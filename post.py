#!/usr/bin/env python

import json
import urllib2
import os

wp_host_ip=os.environ["wp_host_ip"]
wp_username=os.environ["wp_username"]
wp_password=os.environ["wp_password"]

json_data = {
  "type": "page",
  "status": "publish"
}

def publish_page(ip, user, password):
  req = urllib2.Request("http://%s:8080/wp-json/wp/v2/posts"%(ip),
    headers = {
      "Authorization": "Basic " + (user + ":" + password).encode("base64").rstrip(),
      "Content-Type": "application/json",
    }, data = json.dumps(json_data))
  f = urllib2.urlopen(req)

def main():
  title = raw_input("Enter a title: ")
  #content = raw_input("Type some content : ")
  
  print "Type some content (CTRL-D to publish)"
  lines = []
  while True:
    try:
      line = raw_input("")
    except EOFError:
      break
    lines.append(line)
  content = '\n'.join(lines)

  json_data["title"]=title
  json_data["content"]=content

  publish_page(wp_host_ip, wp_username, wp_password)
  print "Page is now published"

if __name__ == "__main__":
    main()
