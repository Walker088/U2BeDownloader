#!/usr/bin/env python3
import requests
import argparse
import getpass
import time
import tqdm
import os
from pprint import pprint

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Authorize the request and store authorization credentials.
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
def saveItems(itemLst):
    with open ('item_id', 'w') as f:
        for item_id in itemLst:
            f.write(item_id + '\n')

def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs

def mine_playlists_list(client, **kwargs):
    kwargs = remove_empty_kwargs(**kwargs)
    response = client.playlists().list(
        **kwargs
    ).execute()
    return [ item['id'] for item in response['items'] ]

def mine_item_inplaylist(client, **kwargs):
    kwargs = remove_empty_kwargs(**kwargs)
    response = client.playlistItems().list(
        **kwargs
    ).execute()
    return [ item['contentDetails']['videoId'] for item in response['items'] ]

def playlist_list(client):
    plLst = mine_playlists_list(client,
        part='snippet,contentDetails',
        mine=True,
        maxResults=50,
        onBehalfOfContentOwner='',
        onBehalfOfContentOwnerChannel='')
    return plLst

def item_id_list(plLst, client):
    result = []
    for itemId in plLst:
        plitem_Lst = mine_item_inplaylist(client,
                            part = 'snippet,contentDetails',
                             maxResults = '50',
                             playlistId = itemId
                            )
        result += plitem_Lst
    return result

def main():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = get_authenticated_service()

    plLst = playlist_list(client)
    itemIdLst = item_id_list(plLst, client)
    saveItems(itemIdLst)
    pprint (itemIdLst)
if __name__ == "__main__":
    main()
#################################################
