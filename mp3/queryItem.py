#!/usr/bin/env python3

import os

def readId():
    with open ('../item_id', 'r') as f:
        Lst = [ line.strip() for line in f ]
    return Lst

def requestData(audio_url):
    os.system('youtube-dl -x --audio-format mp3  --audio-quality 0 {0}'.format(audio_url))
    return True

def downLoad_id(idLst):
    for _id in idLst:
        query = 'https://www.youtube.com/watch?v='+_id
        requestData(query)
    print ("Finished Downloading")
    return True

def main():
    idLst = readId()
    downLoad_id(idLst)

if __name__ == "__main__":
    main()
#############################################################
