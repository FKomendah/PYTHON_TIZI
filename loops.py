#!/usr/bin/python
bundles=1024

while bundles>24:
    print 'Browsing, you have %dMB left'%bundles
    bundles-=24
    if bundles==256:
        print "You have 256MB left"
else:
    print 'done, please recharge'
