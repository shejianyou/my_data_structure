# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:59:24 2019

@author: 佘建友
"""
"""
需要新增加的功能：
(1)、记忆抓取页；
(2)、两次调用浏览器时，都实现无头化；
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#实例化Options对象
chrome_options = Options()
#增加一个参数，告诉浏览器是无头浏览器
chrome_options.add_argument('--headless')
#增加一个参数，告诉浏览器不需要使用GPU渲染
chrome_options.add_argument('--disable-gpu')
#驱动路径，谷歌的存放路径
path = r'E:\Anaconda\chromedriver.exe'
#实例化浏览器对象
browser = webdriver.Chrome(executable_path=path,options=chrome_options)
import requests
from lxml import etree
from urllib.parse import urlencode
import time
from selenium.common.exceptions import TimeoutException#调入异常
import json 

#获取商品列表
def get_productlist(page,s):
    params = {
            'keyword':'内衣女',
            'enc':'utf-8',
            'qrst':'1',
            'rt':'1',
            'stop':'1',
            'spm':'2.1.0',
            'vt':'2',
            'page':page,
            's':s,
            'click':'0'
            }
    url = 'https://search.jd.com/Search?' + urlencode(params)
    
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    js1 = "window.scrollTo(0,10000)"
    browser.execute_script(js1)
    time.sleep(5)#视网络情况而定，设置一个等待时间，等其加载完成
    html = etree.HTML(browser.page_source)
    Llink = html.xpath('//div[@class="p-name p-name-type-2"]/a/@href')
    Llist = ['https:'+ i for i in Llink]#生成器
    get_productinfo(Llist)


#获取每个商品的详细信息和评论
def get_productinfo(Llist):
    i = 0
    for link in Llist:
        product_id = link.split('/')[-1].split('.')[0]
        driver = webdriver.Chrome()
        driver.get(link)
        time.sleep(3)
        product_html = driver.page_source
        doc = etree.HTML(product_html)
        name = str(doc.xpath('//div[@class="sku-name"]/text()'))
        price = str(doc.xpath('//div[@class="dd"]/span[@class="p-price"]/span[@class="price"]/text()'))#多属性中我们使用一个属性
        print(name,price)
#获取商品评论
        headers = {
        
        'Referer': link,
        
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }

        for pagenum in range(1,100):
            print('正在打印第',pagenum,'页')
            try:
                url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv11&productId={1}&score=0&sortType=5&page={0}'.format(pagenum,product_id)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'#用format

                r = requests.get(url,headers=headers)
                time.sleep(3)
            
                data = r.text.strip('fetchJSON_comment98vv11(')#去掉两头两尾
                data = data.strip(');')
                try:
                    datas = json.loads(data)
                    print(datas)
                except:
                    del Llist[i]
                    get_productinfo(Llist)
                    i = i+1
                items = datas.get('comments')
                
                for item in items:
                    content = item.get('content')
                    with open(r'C:\Users\23909\Desktop\京东商品评论.txt','a',encoding='utf-8') as f:
                        f.write(name)
                        f.write(price)
                        f.write(content +'\n')
                        f.close()#
                
            except requests.URLRequired:
                break
                
#程序入口          
def main():
    for page in (x for x in range(1,201,2)):
        s = (page-1)*30 + 1
        get_productlist(page,s)
        s = 0 
        
        
        
        
        
        
        