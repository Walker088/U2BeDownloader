#!usr/bin/env python3

import requests

def requestsToken(url):
    params = {
        client_id : '470167450567-nqadh37h21ssjfumes72g4ioeusv110p.apps.googleusercontent.com ',
        redirect_uri : 'http://localhost:8000',
        scope : 'https://www.googleapis.com/auth/youtube.force-ssl',
        access_type : 'offline',
        include_granted_scopes : 'true',

    }


url = "https://accounts.google.com/o/oauth2/v2/auth"
