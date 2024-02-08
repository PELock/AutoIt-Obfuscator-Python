#!/usr/bin/env python

###############################################################################
#
# AutoIt Obfuscator WebApi interface usage example.
#
# In this example we will verify our activation key status.
#
# Version        : v1.04
# Language       : Python
# Author         : Bartosz Wójcik
# Web page       : https://www.pelock.com
#
###############################################################################

#
# include AutoIt Obfuscator module
#
from autoitobfuscator import AutoItObfuscator

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.autoitobfuscator import AutoItObfuscator

#
# create AutoIt Obfuscator class instance (we are using our activation key)
#
myAutoItObfuscator = AutoItObfuscator("ABCD-ABCD-ABCD-ABCD")

#
# login to the service
#
result = myAutoItObfuscator.login()

#
# result[] array holds the information about the license
#
# result["demo"]          - is it a demo mode (invalid or empty activation key was used)
# result["credits_left"]  - usage credits left after this operation
# result["credits_total"] - total number of credits for this activation code
# result["string_limit"]  - max. script size allowed (it's 1000 bytes for demo mode)
#
if result:

	print(f'Demo version status - {"True" if result["demo"] else "False"}')
	print(f'Usage credits left - {result["credits_left"]}')
	print(f'Total usage credits - {result["credits_total"]}')
	print(f'Max. script size - {result["string_limit"]}')

else:
	print("Something unexpected happen while trying to login to the service.")
