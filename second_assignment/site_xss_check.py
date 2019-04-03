#!/usr/bin/python
import requests as req
import thread

def xsschecker(url,path):
	try:
	        r=req.get(url+path)
	        text=r.text
	        return text
	except Exception as err:
    		pass
xss_scripts=open("xss_scripts.txt","r")
my_urls=["http://192.168.99.100/xss/example1.php?name=","http://192.168.99.100/xss/example2.php?name=","http://192.168.99.100/xss/example3.php?name="]

for xss_script in xss_scripts.readlines():
	for my_url in my_urls:
		my_text=thread.start_new_thread( xsschecker, (my_url, xss_script, ) ) 
		if '>alert("xss")' in str(my_text):
			print "[+]Checking for xss on %s using %s Playload>>>>>>>>>Result:XSS EXISTS!!"%(my_url,xss_script)
		else:
			print "\t[!]Checking for xss on %s using %s Playload>>>>>>>>Result:no xss"%(my_url,xss_script)
