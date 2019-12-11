# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:31:15 2019

@author: 佘建友
"""
#加载单个请求

import requests
import time

headers = {
        'Cookie':'0UtR_2132_saltkey=tVIFB0yy; 0UtR_2132_lastvisit=1575102137; UM_distinctid=16ebb9e379f3c0-0d42c35719cdd4-2393f61-e1000-16ebb9e37a08e4; CNZZDATA1272868653=1686353178-1575102263-https%253A%252F%252Fcn.bing.com%252F%7C1575102263; 0UtR_2132_st_p=0%7C1575106731%7C4e9476467a66824b138615b9247e1b66; 0UtR_2132_viewid=tid_1887; 0UtR_2132_sendmail=1; 0UtR_2132_st_t=0%7C1575107213%7C91c32a84639fe54db6d34f3ba311a95f; 0UtR_2132_forum_lastvisit=D_44_1575105753D_43_1575107213; 0UtR_2132_lastact=1575107215%09index.php%09',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }

def get_main_pages(x):
    url = 'http://www.1jiepai.com/forum-43-{0}.html'.format(x)
    time.sleep(4)
    response = requests.get(url,headers=headers)
    try:
        if response.status_code == 200:
            with open(r'C:\Users\23909\Desktop\jiepai.txt','w',encoding='utf-8') as f:
                f.write(response.text)
            print('抓取成功')
        else:
            return None
    except requests.ConnectionError:
        return None

#从单个请求中抽取出每组图片链接
from lxml import etree

def get_images():
    html = etree.parse(r'C:\Users\23909\Desktop\jiepai.txt',etree.HTMLParser())
    images_link = html.xpath('//div[@class="simgh"]/h2/a/@href')
    images_title = html.xpath('//div[@class="simgh"]/h2/a/text()')
    i = 0
    while i <= len(image_title):
            yield{
                    'title':images_title[i],
                    'link':images_link[i]
                    }
            i += 1
        
          
#从每组图片链接中获取每组图片的每张图片
import os
from hashlib import md5

def download_images(item):
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            }
    path = path = r'C:\Users\23909\Desktop\教务系统设计\\' + item.get('title') 
    if not os.path.exists(path):  
        os.mkdir(path)
    try:
        r = requests.get(item.get('link'),headers=headers)
        if r.status_code == 200:
            with open(r'C:\Users\23909\Desktop\图片.txt','w',encoding='utf-8') as ff:
                ff.write(r.text)
                
            
            
            





            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                