import os, time, errno
from datetime import datetime
from optparse import OptionParser
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "2560,1440"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


def YahooCrawler(keyword, out_path):
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options
    )  

    driver.get("https://images.search.yahoo.com/")

    time.sleep(3)

    first_search_bar = driver.find_element_by_class_name("yschsp")
    first_search_bar.send_keys(keyword)

    submit_button = driver.find_element_by_class_name("ygbt")
    submit_button.click()

    time.sleep(3)

    scroll_iterator = 0
    height = 0
    for i in range(10):
        next_height = driver.execute_script("return document.body.scrollHeight")

        if next_height == height:
            time.sleep(3)
            # break
            try:
                driver.execute_script("window.scrollBy(0,512)")
                time.sleep(3)
                
                find_more = driver.find_element_by_name("more-res")
                find_more.click()
                print("find more clicked")

                time.sleep(3)

            except:
                print("reached end of page")
                # driver.close()
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
        print('making Yahoo screenshots for', keyword, (i+1))
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))
        driver.execute_script("window.scrollBy(0,1280)")
        time.sleep(5)
        scroll_iterator += 1

    driver.close()