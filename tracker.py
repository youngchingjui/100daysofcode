# Daily tracker

import requests
import datetime

URL = "https://github-contributions-api.now.sh/v1/"

# I am running this locally, where I have access to the github_accounts.txt file
usernames = open('github_accounts.txt').read().splitlines()

today = datetime.date.today()
year = today.year
month = today.month
date = today.day - 1

for username in usernames:

    # Adding 'nested' query makes it easier to find today's contributions
    full_path = URL + username + '?format=nested'
    print("Getting contributions for: {}".format(username))

    # Make a GET request
    r = requests.get(url=full_path)
    data = r.json()

    contribution = data['contributions']['contributions'][str(year)][str(month)][str(date)]['count']
    print(contribution)

