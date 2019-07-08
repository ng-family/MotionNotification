#!/usr/bin/python3

import http.client, urllib, requests, time, os
from pathlib import Path

pushoveruser = 'yourusername'
pushovertoken = 'theirprovidedkey
sendimages = 1
targeturl = 'http://url/to/motioneye'
imagepath = '/your/defined/image/storage/'
screenshotimage = '/your/defined/image/storage/default.jpg' #Default image if glob fails

if sendimages:
  time.sleep(60)                                # wait for image to save
  filenames = Path(imagepath).glob('**/*.jpg')
  if filenames:
    screenshotimage = max(filenames, key=os.path.getctime)
  r = requests.post("https://api.pushover.net/1/messages.json",
    data = {
      "token": pushovertoken,                    # Insert app token here
      "user": pushoeveruser,                     # Insert user token here
      "html": "1",                               # 1 for HTML, 0 to disable
      "title": "Motion Detected!",               # Title of the message
      "message": "<b>Front Door</b> camera!",    # Content of the message
      "url": targeturl,                          # Link to be included in message
      "url_title": "View live stream",           # Text for the link
      },
    files = {
      "attachment": ("image.jpg", open(screenshotimage, "rb"), "image/jpeg")
    }
  )
else:
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": pushovertoken,                   # Insert app token here
      "user": pushoeveruser,                    # Insert user token here
      "html": "1",                              # 1 for HTML, 0 to disable
      "title": "Motion Detected!",              # Title of the message
      "message": "<b>Front Door</b> camera!",   # Content of the message
      "url": targeturl,                         # Link to be included in message
      "url_title": "View live stream",          # Text for the link
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
