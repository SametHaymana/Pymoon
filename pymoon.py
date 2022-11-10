#!/bin/python3

import sys
import hashlib
import time
import os

lastHashOfFile = ""

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()





if len(sys.argv) > 2:
	print("You need to spesify py file")
else:
	# Check file is python file
	fileName = sys.argv[1]
	if fileName.split(".")[-1] != "py":
		print("This is not python file")
		exit()

	while True:
		hashOfFile = hash_file(fileName)
		
		if(lastHashOfFile != hashOfFile):
			# File Updated
			print("[pymoon] starting 'python3 " + fileName + "'" )
			os.system('python3 ' + fileName)

		lastHashOfFile = hashOfFile

		time.sleep(2)
