import os, time, errno, pickle, stdiomask
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from urllib.request import urlopen
import json
import csv
import yaml

driver = webdriver.Chrome("C:\\Windows\webdriver\chromedriver.exe")

filename = 'followers.csv'
with open(filename) as csvfile:
    reader = csv.reader(csvfile)

    usernames=[]
    for row in reader:
        username = row[0]
        usernames.append(username)

    usernames1 = []
    for user in usernames:
        username = user.split(',')
        username = username[3]
        usernames1.append(username)

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

# fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
# scroll = 0
# while scroll < xint:
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#     time.sleep(0.1)
#     scroll += 1
#     if scroll == xint/2:
#         print("break")
#         break
#     else:
#         pass

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

# driver.execute_script("window.open('');")


time.sleep(3)
# time.sleep(2)
folllist = []
usernamecounter = 0
for i in range(1, 100):
    usernames2 = str(usernames1[usernamecounter])
    length = int(len(usernames2))
    print(length)
    # lengths = int(length)
    usernames2.split()
    print(usernames2)
    # usernames2.replace(" ","",1)
    usernames2 = usernames2[1,length]
    print(usernames2)
    driver.get("https://www.instagram.com/"+ usernames2 +"/")
    follvalue=followerButton()
    xint = int(follvalue)
    zstr = str(follGet(i))
    print(str(i)+zstr)

    IDstr = str(URL())
    counter += 1
    if IDstr == "None":
        IDstr = "ID limit exceded"
    else:
        pass
    print(IDstr)

    usernamecounter += 1
    time.sleep(0.5)
    folllist.append(zstr + ", " + IDstr)

print(folllist)
time.sleep(3)
with open("followers" + "_user" + ".csv", 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for follower in folllist:
        wr.writerow([follower])

print(folllist)
time.sleep(5)
driver.close