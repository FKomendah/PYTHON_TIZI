#!/usr/bin/python

import requests as req
import sys
import thread

def statuschecker(url,path):
	try:
        	r=req.get(url+path)
        	code=r.status_code
        	return code
	except Exception as error:
		print "Error occurred while testing %s"%url
		pass
def check_url(url):
	if url.endswith("/"):
		pass
	else:
		url=url+"/"
	return url

path_file=open("/usr/share/dirb/wordlists/common.txt","r")

if len(sys.argv)<2:
        print "Usage: %s http://target.url/"%sys.argv[0]
        sys.exit()
else:
        url=sys.argv[1]

url_checked=check_url(url)

for path in path_file.readlines():
        scode= thread.start_new_thread( statuschecker, (url_checked, path, ) )
        print "[+] Checking URL: %s:%s. Status:%s"%(url_checked,path,scode)
