import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent
import ssl
import re
import pandas
import csv

ua = UserAgent()

df = pandas.read_csv('nama-artis-indonesia.csv')

values = df['full_name'].values

#with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/" + "dataset-artis" + '.csv', 'w') as csvfile:
#    fieldnames = ['full_name', 'instagram_username']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()

for i in values[1112:]:

    text = 'instagram' + " " + str(i)
    text = urllib.parse.quote_plus(text)
    number_result = 1

    url = 'https://google.com/search?q=' + text + "&num=" + str(number_result)
    html = requests.get(url, {"User-Agent": ua.random})
    soup = BeautifulSoup(html.text, 'html.parser')

    result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})


    for r in result_div:

        link = r.find('a', href = True)
        links = link['href']
        data = re.search('\/url\?q\=(.*)\&sa',links)


        if data is not None:

            link_true = data.group(1)

            link_final = re.search('https://www.instagram.com/(.*)/', link_true)

            if link_final is None:
                user_ig = "Not Found"
            else:
                user_ig = link_final.group(1)

            print(user_ig)

            with open("/mnt/data/Dataset Face/Instagram Crawling Indonesia + Asia Tenggara/diros/collect-data-instagram/" + "dataset-artis" + '.csv', 'a') as csvfile:
                fieldnames = ['full_name', 'instagram_username']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'full_name': str(i), 'instagram_username' : str(user_ig)})







