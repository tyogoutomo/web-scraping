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
import glob

def convert_amount_followers_or_following(amount):

    amount = str(amount)

    k = amount.find('k')

    comma = amount.find(',')

    m = amount.find('m')
    
    if comma != -1:
        amount = amount.replace(',', '')

    
    if k != -1:
        amount = amount.replace('k', '')
        amount = float(amount) * 1e3
    
    if m != -1:
        amount = amount.replace('m', '')
        amount = float(amount) * 1e6
    
    result = int(amount)

    return result


def check_not_personal_account(full_name):
    
    full_name = str(full_name)
    full_name = full_name.lower()
    
    list_of_online_shop_atribut = ["store", "shoe", "shoes", "bag", "cream", "consignment", "fashion", "lifestyle", "girls", 
    "boys", "life","living", "jastip" , "sepatu", "tas", "klinik", "syariah", "dakwah", "islam", "kristen", "katolik", "budha", 
    "hindu", "wakaf", "buku", "tv", "travel", "event", "organizer", "fanpage", "farm", "tauhiid", "mekkah", "medinah", "daarut", "humas", 
    "bandung", "jakarta", "radio", "wirausaha", "masjid", "sma", "smk", "sd", "smp", "peduli", "bangsa", "sunnah", "herbal", "wisata", "hijrah", "duta", "info"]

    result = any(substring in str(full_name) for substring in list_of_online_shop_atribut)

    return result

def check_selebgram(followers,post_number):

    result = int(followers) > 100e3 and int(post_number) > 75

    return result

def dataset_face(selebgram, online_shop, status_account):

    if selebgram == True and online_shop == False and status_account == "public account":
        result = "YES"

    else:
        result = "NO"

    return result

def sortSecond(val):

    return val[2]



with open("/home/rkb/dir/collect-data-instagram/" + 'result.csv', 'w') as csvfile:
    fieldnames = ['full_name', 'ig_username', 'amount of followers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


dataset_username_ig = []
data_acceptable = []
data_new_ig_username = ["hasil"]

df = pandas.read_csv('dataset-artis-valid.csv')
counter = 0

for index, row in islice(df.iterrows(),1,None):

	dataset_username_ig.append(str(row[1]))


path = "/home/rkb/dir/collect-data-instagram/data_selebgram/RAW/"
dir_list = os.listdir(path) 

list_name = []

for direc in dir_list:

    list_name.append(direc)


list_name.sort()

for direc in list_name:

    path_csv = path + direc
    df_read = pandas.read_csv(path_csv)
    for ind, data in islice(df_read.iterrows(),1,None):
        
        name_full = data[0]
        username_ig = data[1]
        post_number = data[2]
        followers_number = data[3]
        followings_number = data[4]
        account_status = data[5]

        amount_followers = convert_amount_followers_or_following(followers_number)
        amount_post_number = convert_amount_followers_or_following(post_number)
        status_online_shop = check_not_personal_account(name_full)
        status_selebgram = check_selebgram(amount_followers,amount_post_number)
        status_dataset_face = dataset_face(status_selebgram, status_online_shop, account_status)

        if status_dataset_face == "YES":
            

            result = any(substring in str(username_ig) for substring in dataset_username_ig)
            result_new = any(substring in str(username_ig) for substring in data_new_ig_username)
            

            if result == False and result_new == False:
                
               
                data_new_ig_username.append(username_ig)
                data_acceptable.append([name_full,username_ig,amount_followers])

data_acceptable.sort(key=sortSecond)

for dt in data_acceptable:

    full_name_ = dt[0]
    ig_user = dt[1]
    amnt_followers = dt[2]

    with open("/home/rkb/dir/collect-data-instagram/" + 'result.csv', 'a') as csvfile:
        fieldnames = ['full_name', 'ig_username', 'amount of followers']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'full_name': full_name_, 'ig_username': ig_user, 'amount of followers' : str(amnt_followers)})




    

	
