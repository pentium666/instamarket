#!/usr/bin/env python3

import json
import requests

def getuserJSON(username):
    page = requests.get('https://www.instagram.com/'+username+'/media/')
    print(page.text)
