#!/usr/bin/python

import urllib.request
import time

while True:
    def internet(host='https://www.duckduckgo.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    if internet(host='https://www.duckduckgo.com') == True:
        print("Türknet çalışıyor.")
        break
    else:
        print("Türknet uyuyor.")
        time.sleep(15)







