import argparse
import os
import sys
import csv
from instabot import Bot, utils

bot = Bot()
bot.login(username="akuncobacoba123123", password="akuncobacoba123")

target_username = "ruthhstefanie"

user_id = bot.get_user_id_from_username(target_username)
following = bot.api.get_total_followers_or_followings(user_id=user_id, usernames=True, which="followings")

for user in following[:3]:
    
    username = user['username']
    full_name = user['full_name']
    user_id_ = bot.get_user_id_from_username(username)
    data = bot.api.get_user_followings(user_id = user_id_)
    print(data)




"""
    kalau user yang private tidak bisa diextract datanya
    tapi accountnya bisa follow dulu (kayaknya)
    """


