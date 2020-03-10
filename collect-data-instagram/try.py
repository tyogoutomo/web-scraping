import requests
from bs4 import BeautifulSoup

username = "ruthhstefanie"

url = "https://www.instagram.com/" + username + "/"

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
data = soup.find_all('meta', attrs={'property': 'og:description'})

text = data[0].get('content').split()
number_followers = text[0]
number_followings = text[2]
number_posts = text[4]

print(text)
print(number_followers)
