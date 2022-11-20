import requests
import os
import sys
import time 

class steg(object):
    def find(*args, site, data, display_response, content, headers):
        class StegError(Exception):
            pass

        if headers == True:
            r = requests.get(site, data, headers=headers)
        else:
            r = requests.get(site, data)

        if r.status_code == 200 or 100 or 300:
            if display_response == True:
                print(r.status_code)
            else:
                pass
        else:
            raise StegError("Unable to find requested data")

        if content == True:
            print(r.text)
        else:
            pass

    def send(*args, site, data, display_response):
        class StegError(Exception):
            pass

        r = requests.post(site, data)
        if r.status_code == 200 or 100:
            if display_response == True:
                print(r.status_code)
            else:
                pass
        else:
            raise StegError("Unable to send data")
            
            
    def source(*args, site):
        r = requests.get(site)
        print(r.text)


