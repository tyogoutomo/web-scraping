import os, time, errno, pickle, stdiomask
import selenium
from selenium import webdriver
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize

driver = webdriver.Chrome("C:\\Windows\webdriver\chromedriver.exe")
out_path = ''

login_id = ('')
password = ('')

def login_instagram():
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        username_bar = driver.find_element_by_name("username")
        username_bar.send_keys(login_id)

        password_bar = driver.find_element_by_name("password")
        password_bar.send_keys(password)
        time.sleep(2)

        login_button = driver.find_element_by_class_name("L3NKy")
        login_button.click()

    except:
        pass

def postButton():
    try:
        postButtonXpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a'
        post_button = driver.find_element_by_xpath(postButtonXpath)
        print("post button found")
        printPostValue = (post_button.text)
        postValue = printPostValue.split()
        x = postValue[0]
        print(x)
        return x
    except:
        pass
login_instagram()
time.sleep(5)
driver.get("https://www.instagram.com/" + login_id +"/")
time.sleep(3)
postButton()
time.sleep(3)

x=postButton()
xint = int(x) #59

def postGet(n,m):
    try:
        time.sleep(3)
        strn = str(n)
        strm = str(m)
        post_click_Xpath = '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[' + strm + ']/div[' + strn + ']/a'
        post_click = driver.find_element_by_xpath(post_click_Xpath)
        print("xpath found")
        url = post_click.get_attribute("href")
        print("text")
        link = print(url)
        return link
    except:
        pass

time.sleep(3)
folllist = []
i = 1
zint = 1
counter = 1
scrollcounter = 1
# link=postGet()

while i < xint: #1-59
    counter += 1
    scrollcounter += 1
    if i >= 3: #i>3
        i = 1
        zint += 1

    elif i <= 3:
        i += 1
    if scrollcounter == 11:
        SCROLL_PAUSE_TIME = 2.5
        scrollcounter = 1
        fBody  = driver.find_element_by_xpath("//*[@id='react-root']/section")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            break

    zstr = str(postGet(i,zint))
    postURL = print(str(counter)+zstr)
    # driver.get('link')
    
    if counter == xint:
        time.sleep(5)
        break
    else:
        pass
time.sleep(3)
driver.close