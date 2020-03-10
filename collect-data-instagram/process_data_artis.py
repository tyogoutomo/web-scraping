import urllib
from bs4 import BeautifulSoup
from itertools import islice
import requests
import webbrowser
import ssl
import re
import pandas
import csv


df = pandas.read_csv('dataset-artis.csv')


with open("/home/ubuntu/diros/collect-data-instagram/" + "dataset-artis-valid.csv", 'w') as csvfile:
	fieldnames = ['full_name', 'instagram_username', 'username_valid']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()


for index, row in islice(df.iterrows(),1,None):

	full_name = row[0]
	username = row[1]
	
	
	if username.find("/") != -1:

		valid_user = "NO"

	else:
		valid_user = "YES"

		
	with open("/home/ubuntu/diros/collect-data-instagram/" + "dataset-artis-valid.csv", 'a') as csvfile:
		fieldnames = ['full_name', 'instagram_username', 'username_valid']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'full_name': str(full_name), 'instagram_username' : str(username), 'username_valid' : valid_user})

	
