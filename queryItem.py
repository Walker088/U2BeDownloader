#!/usr/bin/env python3

import requests

def requestData():
    params = {
        'part' : 'snippet,contentDetails',
        'mine' : 'True',
        'maxResults' : 50
    }
    r = requests.get('https://www.googleapis.com/youtube/v3/playlists', data=params)
    print (r.text)

requestData()

#############################################################
