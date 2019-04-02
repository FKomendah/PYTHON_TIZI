#!/usr/bin/python
try:
        fh=open("testfile2","r")
        fh.write("This is my test file for exception handling")
except IOError:
        print "Error: can\'t find file or read data"
else:
        print "Written content in the file successfully"
        fh.close()
