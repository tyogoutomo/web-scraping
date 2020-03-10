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
#import instaloader
from instaloader import Instaloader, Profile



username="akuncobacoba123123"
password="akuncobacoba123"

L = Instaloader()
L.login(username, password)

target = 'aliandoo'

profile = Profile.from_username(L.context, target)

print(profile)
