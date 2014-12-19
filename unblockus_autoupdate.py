#!/usr/bin/python
#
# Unblock-Us Update-Script
#                                                                              
# This script automatically sends your current IP adress to the Unblock-Us api.
# It can be used to update your IP adress via cron.
#                             
# Author:       Timo Schlueter
# Mail:         me@timo.in       
# Web:          www.timo.in
# Twitter:      twitter.com/tmuuh
#                  
# Version:      0.3      
# Date:         19-12-2014
#                                                                         
# Notes:        I am not affiliated with Unblock-Us
#

# Modules
import sys
import urllib2

# Variables (user specific)
userlogin = "email@example.com"
userpassword = "password"

# Environtment
apiurl = "https://api.unblock-us.com/login"

if not (userlogin):
	print "No username set."
	exit(1)
elif not (userpassword): 
	print "No password set."
	exit(1)
else:
	request = urllib2.urlopen(apiurl + "?" + userlogin + ":" + userpassword)
	response = request.read()	
	request.close()

	if (response == "active"):
		print "IP address is active. You are good to go!"
		exit(0)
	elif (response == "bad_password"):
		print "Wrong username or password."
		exit(1)
	elif (response == "not_found"):
		print "Username not found."
		exit(1)
	else:
		print "Unknown error. Check api url or documentantion."
		exit(1)
