import pandas
from itertools import islice
import csv



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

def check_online_shop(full_name):
    
    full_name = str(full_name)
    full_name = full_name.lower()
    
    list_of_online_shop_atribut = ["store", "shoe", "shoes", "bag", "cream", "consignment", "fashion", "lifestyle", "girls", "boys", "life", "living", "jastip" , "sepatu", "tas"]

    result = any(substring in str(full_name) for substring in list_of_online_shop_atribut)

    return result

def check_selebgram(followers):

    result = int(followers) > 5e3

    return result

def dataset_face(selebgram, online_shop, status_account):

    if selebgram == True and online_shop == False and status_account == "public account":
        result = "YES"

    else:
        result = "NO"

    return result

target_username = "ruthhstefanie"

with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/data_selebgram/FILTER/" + target_username + '.csv', 'w') as csvfile:
    fieldnames = ['full_name', 'ig_username', 'followers', 'online_shop', 'selebgram', 'dataset_face']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


df = pandas.read_csv('/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/data_selebgram/RAW/' + target_username + '.csv', header = None)


for index, row in islice(df.iterrows(),1,None):
    full_name = str(row[0])
    username = str(row[1])
    post = str(row[2])
    followers = row[3]
    following = str(row[4])
    status_account = str(row[5])


    amount_followers = convert_amount_followers_or_following(followers)
    status_online_shop = check_online_shop(full_name)
    status_selebgram = check_selebgram(amount_followers)
    status_dataset_face = dataset_face(status_selebgram, status_online_shop, status_account)

    with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/data_selebgram/FILTER/" + target_username + '.csv', 'a') as csvfile:
        fieldnames = ['full_name', 'ig_username', 'followers', 'online_shop', 'selebgram', 'dataset_face']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'full_name': full_name, 'ig_username': username, 'followers' : str(followers), 'online_shop' : status_online_shop, 'selebgram' : status_selebgram, 'dataset_face' : status_dataset_face})












