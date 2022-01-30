# coding:utf8

from selenium import webdriver
import time,re
import requests
from bs4 import BeautifulSoup

t = time.time() 

lognames = '13110292131' #帐号
logpass = '6404556306'#密码
yaohuo = 'http://yaohuo.me'
counts = 2 #爬取最新帖子页数
cookie = None
page = 1
CONTENT = ['吃', '吃!', '吃了', '吃,']
a = 0 #CONTENT 1-4位置
n = 0 #成功次数
driver = webdriver.Firefox()

def login():    
    driver.get("https://yaohuo.me/waplogin.aspx")
    time.sleep(0.5)
    driver.find_element_by_name('logname').send_keys(lognames)
    driver.find_element_by_name('logpass').send_keys(logpass)
    time.sleep(0.5)
    driver.find_element_by_xpath('//button').click()
    time.sleep(5)
login()
while True:
    driver.get('https://yaohuo.me/bbs/book_list.aspx?action=new&siteid=1000&classid=0&getTotal=2020&page='+str(page))
    ps = driver.page_source
    ps = BeautifulSoup(ps, 'html.parser')
    links = ps.find_all('div', class_=re.compile(r'line\d'))
    for link in links:
        if (str(link).find('/NetImages/li.gif')) != -1:
            url = yaohuo + re.findall(r'href="(.*)html', str(link))[0] + 'html'
            print(url)
            f = open("log.txt") 
            ff = f.read()            
            f.close()
            print(ff.find(url))
            if ff.find(url) == -1:
                driver.get(url)
                ps2 = driver.page_source
                if ps2.find('余0') == -1:                                    
                    driver.find_element_by_name('content').send_keys(CONTENT[a])
                    time.sleep(1)  
                    driver.find_element_by_name('g').click()
                    print('吃到了')  
                    if a == 3:
                        a -= 3
                    else:
                        a += 1
                    time.sleep(5)    

                    f = open("log.txt",'a+') 
                    f.write(url)
                    f.write("\n")
                    f.close()
                    time.sleep(2)
                    n = n + 1
                    print ("成功吃肉次数：%d"  %n)
                    st = ("成功吃肉次数：%d"  %n)
                    driver.get('http://wxpusher.zjiecode.com/api/send/message/?appToken=AT_xoZeIE7CuT9IXjnFiCZlpbPJvLqDvrbu&content=%s&uid=UID_Lzo4bqvfU8JMzzbQYK4giM5Q2cCT&url=%s' %(st,url))
                    time.sleep(2)
                else:
                    f = open("log.txt",'a+') 
                    f.write(url)
                    f.write("\n")
                    f.close()
                    time.sleep(2)
                    print ("没有肉可以吃!")
            else:
                 print('已经扫描过该帖！')
                 
                 

    print('第%d页' %page)
    if page < counts:
        page += 1
    else:
        page = page - 9
    print('--------------------')
    time.sleep(20)
           
# try:                                                          
#     f = driver.find_elements_by_xpath(".//img[@src='/NetImages/li.gif']")
    
#     print('成功')
# except:
#     print('没找到')


# while page <= counts:
#     print(page) 
#     driver.get('https://yaohuo.me/bbs/book_list.aspx?action=new&siteid=1000&classid=0&getTotal=2020&page=' + str(page))
#     time.sleep(1)
#     try:
#         driver.find_element_by_xpath('//*[@img]').click
#         url = driver.current_url
#         print(url)
#     except:
#         page += 1
    


print(time.time()-t)
