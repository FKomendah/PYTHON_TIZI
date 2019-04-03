#!/usr/bin/python
import requests as req
import sys

def statuschecker(url,path):
	'''comment here'''
        r=req.get(url+path)
        code=r.status_code
        return code


path_file=open("/usr/share/dirb/wordlists/common.txt","r")


try:
	if len(sys.argv)<2:
        	print "Usage: %s http://target.url"%sys.argv[0]
        	sys.exit()
	else:
        	url=sys.argv[1]
	for path in path_file.readlines():
        	scode=statuschecker(url,path)
        	print "[+] Checking URL: %s:%s. Status:%s"%(url,path,scode)

except Exception as err:
	print "Check that URL"
	print (err)
