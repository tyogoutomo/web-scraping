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

bot = Bot()
bot.login(username="akuncobacoba123123", password="akuncobacoba123")

target_username = "ruthhstefanie"

user_id = bot.get_user_id_from_username(target_username)
following = bot.api.get_total_followers_or_followings(user_id=user_id, usernames=True, which="followings")


with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/data_selebgram/" + target_username + '.csv', 'w') as csvfile:
    fieldnames = ['full_name', 'ig_username', 'post', 'followers', 'followings', 'public/private']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

for user in following[:10]:
    
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

    
    with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/data_selebgram/" + target_username + '.csv', 'a') as csvfile:
        fieldnames = ['full_name', 'ig_username', 'post', 'followers', 'followings', 'public/private']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'full_name': full_name, 'ig_username': username, 'post' : str(number_posts), 'followers' : str(number_followers), 'followings' : str(number_followings), 'public/private' : status_account})


"""
kalau user yang private tidak bisa diextract datanya
tapi accountnya bisa follow dulu (kayaknya)

masalah kecepatan ini cepat walaupun internet lambat
kemudian di bagian full name
untuk membedakan nama online shop dengan account pribadi dengan keywords seperti bag, shoes, online, etc
"""

