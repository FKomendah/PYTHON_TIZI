#!/usr/bin/python
bundles=1024

while bundles>24:
    	print 'Browsing, you have %dMB left'%bundles
    	bundles-=24
	if bundles ==256:
		print "Your bundles is less than 256MB. Enjoy browsing with safaricom"
else bundles>24:
    print 'done, please recharge'
