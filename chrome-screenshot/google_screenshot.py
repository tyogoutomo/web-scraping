import os, time, errno, urllib.request
from tqdm import tqdm
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

    links_list = []

    i = 0
    try_count = 0

    print("generating links for", keyword)
    for i in tqdm(range(150)):
    # while i <= 150:
        try:
            i += 1
            found_element = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]')
            found_element.click()

            time.sleep(2)

            found_href = found_element.get_attribute("href")
            img_true = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/a/img')
            img_src = img_true.get_attribute('src')

            # links_list.append(found_href)
            links_list.append(img_src)

            if try_count == 5:
                print("no more links")
                break
        except:
            try_count += 1
            pass

    for index,links in enumerate(links_list):
        driver.get(links)

        save_path = os.path.join(out_path, keyword)
        try:
            os.makedirs(save_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        print('making Google screenshots for', keyword, index)
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))

    driver.close()