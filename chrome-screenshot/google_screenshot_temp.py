import os, time, errno
from datetime import datetime
from optparse import OptionParser
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "2560,1440"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

def GoogleCrawler(keyword, out_path):
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options
    )

    driver.get("https://images.google.com/")

    time.sleep(3)

    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(keyword)

    search_button = driver.find_element_by_class_name("Tg7LZd")
    search_button.click()

    time.sleep(3)

    scroll_iterator = 0
    height = 0
    for i in range(100):
        next_height = driver.execute_script("return document.body.scrollHeight")

        if next_height == height:
            time.sleep(3)
            try:
                find_more = driver.find_element_by_class_name("mye4qd")
                find_more.click()
                print("find more clicked")

                time.sleep(3)
                driver.execute_script("window.scrollBy(0,1280)")

            except:
                print("reached end of page")
                break

        height = driver.execute_script("return document.body.scrollHeight")

        save_path = os.path.join(out_path, keyword)
        try:
            os.makedirs(save_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        print('making Google screenshots for', keyword, (i+1))
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))
        driver.execute_script("window.scrollBy(0,1280)")
        time.sleep(5)

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))
        driver.execute_script("window.scrollBy(0,1280)")
        time.sleep(5)
        scroll_iterator += 1

    driver.close()