import os, time, errno

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

driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH,
    chrome_options=chrome_options
)  

out_path = "./downloads/"
driver.get("https://images.search.yahoo.com/")

# ele_login = driver.find_elements_by_class_name(".Ls00D")
# if ele_login:
#     ele_login.click()

# Returns first element with matching class
first_search_bar = driver.find_element_by_class_name("yschsp")
first_search_bar.send_keys("jokowi")

submit_button = driver.find_element_by_class_name("ygbt")
submit_button.click()

driver.save_screenshot(out_path + "test1.png")

# for elements in first_search_bar:
#     a_element = driver.find_element_by_tag_name("a")
#     links = a_element.get_attribute("href")
#     print(links)

# print(first_search_bar)

# all_spans = driver.find_elements_by_xpath("//div[@class='v1Nh3']")
# for span in all_spans:
#     print(span)