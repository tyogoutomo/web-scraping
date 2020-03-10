## IMPORT DEPENDENCY
import sys, os, json, time, cv2, errno
from tqdm import tqdm
from PIL import Image
from selenium import webdriver
from datetime import datetime
from setuptools import sandbox
from distutils.core import run_setup

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
WINDOW_SIZE = "1280,720"
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

## SET PATH DOWNLOAD IMAGE, DAN FILE EXTENSIONS YANG DIINGINKAN
download_path = './downloads/'

## CLONE REPO PROGRAM google-images-download
google_git = "git clone https://github.com/luqmanr/google-images-download.git ./google_images_download"
setup_py = "python setup.py install"

os.system(google_git)
run_setup('./google_images_download/setup.py', script_args=sys.argv[1:],stop_after='run')
# os.rename('./google-images-download', 'google_images_download')
# os.chdir('./google_images_download')
print(os.getcwd())
from google_images_download.google_images_download import google_images_download
os.chdir('../')

response = google_images_download.googleimagesdownload()

daftar_nama = [
    "prabowo"
]

## DEFINISI FUNGSI crawling UNTUK MENDOWNLOAD IMAGES DARI GOOGLE
def google_crawling(keyword):
    keyword_format = keyword_formatter(keyword)
    print('keyword_format =', keyword_format)
    paths = response.download(keyword_format)   #MASUKIN ARGUMENT KE LIBRARY google-images-download

## MENGUBAH LIST daftar_nama MENJADI LIST BARU YANG DIMASUKKAN KE LIBRARY google-images-download
def keyword_formatter(nama):
    json_nama = {"Records":[]}
    if len(str(nama)) > 1:
        json_nama["Records"].append({
                    "keywords" : str(nama), 
                    "limit" : 20,
                    'silent_mode' : True,
                    'chromedriver' : '/usr/lib/chromium-browser/chromedriver'})
    return json_nama['Records']
    print('keyword =',json_nama)

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

if __name__ == '__main__':
    for nama in daftar_nama:
        print('downloading for',nama)
        google_crawling(nama)