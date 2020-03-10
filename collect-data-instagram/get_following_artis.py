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

bot = Bot()
bot.login(username="akuncobacoba123123", password="akuncobacoba123")


df = pandas.read_csv('/home/ubuntu/diros/collect-data-instagram/get_data/dataset-artis-valid.csv')


for index, row in islice(df.iterrows(),1,None):

	full_name = str(row[0])
	target_username = str(row[1])
	valid_user = str(row[2])
	
	if valid_user == "YES":

		user_id = bot.get_user_id_from_username(target_username)
		following = bot.api.get_total_followers_or_followings(user_id=user_id, usernames=True, which="followings")

		with open("/home/ubuntu/diros/collect-data-instagram/RAW/" + full_name + '.csv', 'w') as csvfile:
			fieldnames = ['full_name', 'ig_username', 'post', 'followers', 'followings', 'public/private']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

		for user in following:

			username = user['username']
			full_name = user['full_name']
			user_id_ = bot.get_user_id_from_username(username)
			data_following = bot.api.get_total_followers_or_followings(user_id=user_id_, usernames=True, which="followings")

			url = "https://www.instagram.com/" + username + "/"

			ctx = ssl.create_default_context()
			ctx.check_hostname = False
			ctx.verify_mode = ssl.CERT_NONE
			html = urllib.request.urlopen(url, context=ctx).read()
			soup = BeautifulSoup(html, 'html.parser')
			data = soup.find_all('meta', attrs={'property': 'og:description'})


			text = data[0].get('content').split()
			number_followers = text[0]
			number_followings = text[2]
			number_posts = text[4]

			if data_following == []:
				status_account = "private account"

			else:
				status_account = "public account"


			with open("/home/ubuntu/diros/collect-data-instagram/RAW/" + full_name + '.csv', 'a') as csvfile:
				fieldnames = ['full_name', 'ig_username', 'post', 'followers', 'followings', 'public/private']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writerow({'full_name': full_name, 'ig_username': username, 'post' : str(number_posts), 'followers' : str(number_followers), 'followings' : str(number_followings), 'public/private' : status_account})



