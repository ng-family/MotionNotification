#!/usr/bin/python3

import http.client, urllib, requests, time, os
from pathlib import Path

pushovertoken

sendimages = 1

if sendimages:
  imagepath = '/your/defined/image/storage/default.jpg'
  time.sleep(60)                                # wait for image to save
  filenames = Path('/your/defined/image/storage/').glob('**/*.jpg')
  if filenames:
    imagepath = max(filenames, key=os.path.getctime)
  r = requests.post("https://api.pushover.net/1/messages.json",
    data = {
      "token": "1-2-3-4-5? That's the stupidest",# Insert app token here
      "user": "Pushover provided username",      # Insert user token here
      "html": "1",                               # 1 for HTML, 0 to disable
      "title": "Motion Detected!",               # Title of the message
      "message": "<b>Front Door</b> camera!",    # Content of the message
      "url": "http://url/to/motioneye",          # Link to be included in message
      "url_title": "View live stream",           # Text for the link
      },
    files = {
      "attachment": ("image.jpg", open(imagepath, "rb"), "image/jpeg")
    }
  )
else:
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": "az",# Insert app token here
      "user": "u7", # Insert user token here
      "html": "1",                              # 1 for HTML, 0 to disable
      "title": "Motion Detected!",              # Title of the message
      "message": "<b>Front Door</b> camera!",   # Content of the message
      "url": "http://1/",      # Link to be included in message
      "url_title": "View live stream",          # Text for the link
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
