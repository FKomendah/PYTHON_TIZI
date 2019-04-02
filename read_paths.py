#!/usr/bin/python
import requests as req
def statuschecker(url,path):
	r=req.get(url+path)
	code=r.status_code
	return code
path_file=open("paths.txt","r")
url="https://www.strathmore.edu/"
for path in path_file.readlines():
	scode=statuschecker(url,path)
	print "[+] Checking URL: %s:%s. Status:%s"%(url,path,scode)
