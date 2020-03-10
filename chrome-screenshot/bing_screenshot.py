import os, time, errno
from datetime import datetime
from optparse import OptionParser
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "3840,2160"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


def BingCrawler(keyword, out_path):
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options
    ) 

    bing_url = "https://www.bing.com/images/search?q="
    keywords_link = bing_url + keyword
    make_screenshot(keywords_link, keyword, driver, out_path)

    driver.close()

def make_screenshot(keywords_link, keyword, driver, out_path):
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"') 

    print('opening page')
    driver.get(keywords_link)

    scroll_iterator = 0
    height = 0
    for i in range(10):
        next_height = driver.execute_script("return document.body.scrollHeight")

        if next_height == height:
            time.sleep(3)
            # break
            try:
                driver.execute_script("window.scrollBy(0,1080)")
                time.sleep(3)
                
                find_more = driver.find_element_by_class_name("btn_seemore")
                find_more.click()
                print("find more clicked")

                time.sleep(3)

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
        print('making Bing screenshots for', keyword, (i+1))
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))
        driver.execute_script("window.scrollBy(0,1920)")
        time.sleep(5)
        scroll_iterator += 1