# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:53:24 2019

@author: 佘建友
"""
from selenium import webdriver
from lxml import etree
import csv
from urllib.parse import quote
browser = webdriver.Chrome()
browser.set_page_load_timeout(20)

def get_list(page,index,city):
    url = 'https://www.ciweishixi.com/search?s_c=&s_i=&s_j=&s_s=&s_w=&s_e=&s_p=&s_work=&city={1}&key=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&time=&areaname={2}&page={0}'.format(page,index,city)
    browser.get(url)
    html = etree.HTML(browser.page_source)
    with open(r'C:\Users\23909\Desktop\刺猬实习.csv','a',encoding='utf-8') as csvfile:
        detail_url = html.xpath('//div[@class="info"]/div[@class="major"]/a/@href')
        title = html.xpath('//div[@class="info"]/div[@class="major"]/a/code/text()')
        time = html.xpath('//div[@class="info"]/div[@class="major"]/time/text()')
        salary = html.xpath('//div[@class="info"]/div[@class="aide"]/span[1]/text()')
        xueli = html.xpath('//div[@class="info"]/div[@class="aide"]/span[2]/text()')
        days = html.xpath('//div[@class="info"]/div[@class="aide"]/span[3]/text()')
        writer = csv.writer(csvfile)
        for i in range(0,10):
            browser.get(detail_url[i])
            doc = etree.HTML(browser.page_source)
            zhize = doc.xpath('//div[@class="item"][1]/p/text()')
            yaoqiu = doc.xpath('//div[@class="item"][2]/p/text()')
            writer.writerow([title[i],time[i],salary[i],xueli[i],days[i],zhize[i],yaoqiu[i]])
            print(title[i],time[i],salary[i],xueli[i],days[i],zhize[i],yaoqiu[i])
        writer.close()
  
if __name__ == '__main__':
    area_dict = [[321,'上海'],[76,'广州'],[77,'深圳'],[52,'北京']]
    for area in area_dict:
        area_bianma = quote(area[1])
        for page in range(0,5): 
            get_list(page,area[0],area_bianma)
            print('='*5+'正在爬取',area[1],'的信息''='*5)
            
        
    