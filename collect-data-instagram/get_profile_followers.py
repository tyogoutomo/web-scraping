import csv, os
from instaloader import Instaloader, Profile
loader = Instaloader()

login_name = "" ## MASUKIN USERNAME INSTAGRAM LOGIN
target_profile = "" ## MASUKIN USERNAME INSTAGRAM YANG INGIN DI CRAWLING

# login
try:
    loader.load_session_from_file(login_name)
except FileNotFoundError:
    loader.context.log("Session file does not exist yet - Logging in.")
if not loader.context.is_logged_in:
    loader.interactive_login(login_name)
    loader.save_session_to_file()

profile = Profile.from_username(loader.context, target_profile)
followers = profile.get_followers()

loader.context.log()
loader.context.log('Profile {} has {} followers:'.format(profile.username, profile.followers))
loader.context.log()

with open('test.csv', 'w', newline='') as csvfile: ## GANTING 'test.csv' DENGAN FILE NAME YANG DIINGINKAN
    writer = csv.writer(csvfile)
    for follower in followers:
        loader.context.log(follower.username, flush=True)
        writer.writerow([follower.username])