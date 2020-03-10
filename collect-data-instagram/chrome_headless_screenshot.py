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

daftar_nama = [
    "luqmanr"
]

base_url = "https://www.instagram.com/"
out_path = "./downloads/"

def main(keywords_list, base_url):
    for keywords in keywords_list:
        # print(nama)
        keywords_link = base_url + keywords
        # print(keywords_link)
        make_screenshot(keywords_link, keywords)
        time.sleep(50)


def make_screenshot(keywords_link, keywords):
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"')

    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options
    )  

    print('opening page')
    driver.get(keywords_link)

    scroll_iterator = 0

    for i in range(10):
        print('making screenshots for ', keywords, i)
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        save_path = out_path + keywords + "/"
        try:
            os.makedirs(save_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        driver.save_screenshot(save_path + str(scroll_iterator) + ".png")
        driver.execute_script("window.scrollBy(0,1080)")
        time.sleep(5)
        scroll_iterator += 1
    
    driver.close()

if __name__ == '__main__':
    
    main(daftar_nama, base_url)
    # make_screenshot(instagram_url)


    # usage = "usage: %prog [options] <url> <output>"
    # parser = OptionParser(usage=usage)

    # (options, args) = parser.parse_args()

    # if len(args) < 2:
    #     parser.error("please specify a URL and an output")

    