import argparse
import os
import sys
import csv
import urllib.parse
import urllib.error
import ssl
import requests
from bs4 import BeautifulSoup
from instabot import Bot, utils
import pandas
from itertools import islice
import random
import re
import json
import time

BASE_URL = 'https://www.instagram.com/accounts/login/'
LOGIN_URL = BASE_URL + 'ajax/'

headers_list = [
        "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101"\
        " Firefox/41.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)"\
        " AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2"\
        " Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"\
        " Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"\
        " (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"\
        " Edge/12.246"
        ]


USERNAME = "akuncobacoba123123"
PASSWD = "akuncobacoba123"
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"
session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})    
req = session.get(BASE_URL)    
soup = BeautifulSoup(req.content, 'html.parser')    
body = soup.find('body')

pattern = re.compile('window._sharedData')
script = body.find("script", text=pattern)

script = script.get_text().replace('window._sharedData = ', '')[:-1]
data = json.loads(script)

csrf = data['config'].get('csrf_token')
login_data = {'username': USERNAME, 'password': PASSWD}
session.headers.update({'X-CSRFToken': csrf})
login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
login.content

bot = Bot()
bot.login(username="akuncobacoba123123", password="akuncobacoba123")


df = pandas.read_csv('dataset-artis-valid.csv')

for index, row in islice(df.iterrows(),1,None):

	if index > 39 :	

		full_name = str(row[0])
		target_username = str(row[1])
		valid_user = str(row[2])

		full_name = full_name.replace(" ", "-")

		print(target_username)
		
		time.sleep(100)

		if valid_user == "YES":

			time.sleep(10)

			user_id = bot.get_user_id_from_username(target_username)
			following = bot.api.get_total_followers_or_followings(user_id=user_id, usernames=True, which="followings")

			with open("/home/ubuntu/diros/collect-data-instagram/data_selebgram/RAW/" + full_name + '.csv', 'w') as csvfile:
				fieldnames = ['full_name', 'ig_username', 'post', 'followers', 'followings', 'public/private']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()			
			
			for user in following:

				

				username = user['username']
				full_name_following = user['full_name']
				user_id_ = bot.get_user_id_from_username(username)
				data_following = bot.api.get_total_followers_or_followings(user_id=user_id_, usernames=True, which="followings")
				
				time.sleep(5)
				url = "https://www.instagram.com/" + username + "/"

				html = session.get(url)
				soup = BeautifulSoup(html.content, 'html.parser')
				data = soup.find_all('meta', attrs={'property': 'og:description'})

				print(html)
			
				if data != []:

					text = data[0].get('content').split()
					number_followers = text[0]
					number_followings = text[2]
					number_posts = text[4]

					if data_following == []:
						status_account = "private account"

					else:
						status_account = "public account"


					with open("/home/ubuntu/diros/collect-data-instagram/data_selebgram/RAW/" + full_name + '.csv', 'a') as csvfile:
						fieldnames = ['full_name', 'ig_username', 'post', 'followers', 'followings', 'public/private']
						writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
						writer.writerow({'full_name': full_name_following, 'ig_username': username, 'post' : str(number_posts), 'followers' : str(number_followers), 'followings' : str(number_followings), 'public/private' : status_account})

	



