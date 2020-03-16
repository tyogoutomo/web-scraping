import os, time, errno, pickle, stdiomask
from selenium import webdriver
import selenium
import re
from urllib.request import urlopen
import json
import csv
import yaml

driver = webdriver.Chrome("C:\\Windows\webdriver\chromedriver.exe")

login_id = input('Your IG Account Username: ')
password = input('Your IG Account Password: ')

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

def followerButton():
    try:
        follButtonXpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        follower_button = driver.find_element_by_xpath(follButtonXpath)
        print("button found")
        print(follower_button.text)
        follower_button.click()
        print("button clicked")
        printfoll = (follower_button.text)
        follValue = printfoll.split()
        print(follValue[0])
        follvalue = follValue[0]
        return follvalue
    except:
        pass

login_instagram()
time.sleep(5)
account = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
acc = account.get_attribute('href')
driver.get(acc)
time.sleep(3)

follvalue=followerButton()
xint = int(follvalue)
time.sleep(3)

fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
while scroll < xint:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(0.1)
    scroll += 1
    if scroll == xint/2:
        print("break")
        break
    else:
        pass

def follGet(n):
    try:
        str_n = str(n)
        follXpath = '/html/body/div[4]/div/div[2]/ul/div/li[' + str_n + ']/div/div[1]/div[2]/div[1]/a'
        follower_name = driver.find_element_by_xpath(follXpath)
        time.sleep(0.2)
        follvalue = (follower_name.text)
        return follvalue
    except:
        pass
counter = 0
def URL():
    max = 100  #maximal userID to take (to avoid account block by Instagram)
    while counter <= max:
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.instagram.com/"+zstr+"/?__a=1")
        time.sleep(0.3)
        userID=driver.find_element_by_xpath('/html/body/pre')
        user=userID.get_attribute('innerHTML')
        s=user
        y=yaml.load(s, Loader=yaml.FullLoader)
        l=(y.get("logging_page_id"))
        IGid=(l.split('_'))
        IGidVal = IGid[1]
        driver.switch_to.window(driver.window_handles[0])
        if counter >= max:
            print("ID Limit exceded")
            break
        return IGidVal

def myURL():
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.instagram.com/"+login_id+"/?__a=1")
    time.sleep(0.5)
    userID=driver.find_element_by_xpath('/html/body/pre')
    user=userID.get_attribute('innerHTML')
    s=user
    y=yaml.load(s, Loader=yaml.FullLoader)
    l=(y.get("logging_page_id"))
    IGid=(l.split('_'))
    myIGidVal = IGid[1]
    driver.switch_to.window(driver.window_handles[0])
    return myIGidVal

driver.execute_script("window.open('');")
myIGidVal = str(myURL())
print(myIGidVal)
time.sleep(2)
folllist = []
for i in range(1, xint):
    zstr = str(follGet(i))
    print(str(i)+zstr)

    IDstr = str(URL())
    counter += 1
    if IDstr == "None":
        IDstr = "ID limit exceded"
    else:
        pass
    print(IDstr)
    
    time.sleep(0.5)
    folllist.append("#type your name here, "+login_id+", "+myIGidVal+", "+zstr+", "+IDstr)

# folllist = []
# for i in range(1, xint):
#     zstr = str(follGet(i))
#     print(str(i)+zstr)
#     folllist.append("#TypeYourNameHere, "+login_id+", "+z.str)
print(folllist)
time.sleep(3)
with open('followers.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for follower in folllist:
        wr.writerow([follower])
time.sleep(5)
driver.close