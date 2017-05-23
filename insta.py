#!/usr/bin/env python3

import json
import requests
import csv

def getuserJSON(username):
    try:
        page = requests.get('https://www.instagram.com/'+username+'/media/')
    except JSONDecodeError:
        print('user not found')
    return json.loads(page.text)

def getuserCSV(username):
    data = getuserJSON(username)

    with open(username+'.csv', 'w') as outfile:
        fieldnames =['time', 'likes', 'link']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for photo in data['items']:
            time = photo['created_time']
            likes = photo['likes']['count']
            link = photo['images']['standard_resolution']['url']
            writer.writerow({'time': time, 'likes': likes, 'link': link})
