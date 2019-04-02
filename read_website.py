#!/usr/bin/python
import requests as req
urls=["https://google.com","https://fantasy.premierleague.com","https://www.pluralsight.com"]
for url in urls:
	r=req.get(url)
	print "The status code for %s is %s" %(url,r.status_code)
