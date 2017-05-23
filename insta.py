#!/usr/bin/env python3

import json
import requests
import csv
import sys

class User:
    def __init__(self, username):
        data = getuserJSON(username)
        if(data):
            self.data = getuserJSON(username)
        else:
            raise LookupError
    def getaveragelikes(self, start=-sys.maxsize, end=sys.maxsize):
        """returns the average number likes between start and end"""
        total = n = 0
        for photo in self.data['items']:
            if int(photo['created_time']) > start and int(photo['created_time']) < end:
                total += photo['likes']['count']
                n += 1
        return total/n

def getuserJSON(username):
    """returns user object from username"""
    page = requests.get('https://www.instagram.com/'+username+'/media/')
    try:
        data = json.loads(page.text)
        return data
    except json.decoder.JSONDecodeError:
        print('user not found')
        return False

def getuserCSV(username):
    """outputs a csv file with likes and timestamps from username"""
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
