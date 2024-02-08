#!/usr/bin/env python

###############################################################################
#
# AutoIt Obfuscator WebApi interface usage example.
#
# In this example we will obfuscate sample source with default options.
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
# should the source code be compressed (both input & compressed)
#
myAutoItObfuscator.enableCompression = True

#
# detect debuggers attached to the application process
#
myAutoItObfuscator.antiDebug = True

#
# detect popular virtual machines
#
myAutoItObfuscator.antiVM = True

#
# detect sandboxes
#
myAutoItObfuscator.antiSandbox = True

#
# detect CPU emulators
#
myAutoItObfuscator.antiEmulator = True

#
# generate random integer values
#
myAutoItObfuscator.randomIntegers = True

#
# generate random value characters
#
myAutoItObfuscator.randomCharacters = True

#
# generate random anti regular expression values
#
myAutoItObfuscator.randomAntiRegex = True

#
# generate arrays with random values
#
myAutoItObfuscator.randomArrays = True

#
# generate multidimensional arrays with random values
#
myAutoItObfuscator.randomArraysMultidimensional = True

#
# generate functions that returns random values
#
myAutoItObfuscator.randomFunctions = True

#
# generate autostarted random values
#
myAutoItObfuscator.randomAutostarted = True

#
# change linear code execution flow to nonlinear version
#
myAutoItObfuscator.mixCodeFlow = True

#
# rename variable names to random string values
#
myAutoItObfuscator.renameVariables = True

#
# rename function names to random string values
#
myAutoItObfuscator.renameFunctions = True

#
# rename function names in function calls
#
myAutoItObfuscator.renameFunctionCalls = True


#
# resolve WinApi constants to numerical values
#
myAutoItObfuscator.resolveConstants = True

#
# encrypt numbers into arithmetic and boolean expressions
#
myAutoItObfuscator.cryptNumbers = True

#
# split strings into series of random sized substrings
#
myAutoItObfuscator.splitStrings = True

#
# modify strings using built-it AutoIt string functions
#
myAutoItObfuscator.modifyStrings = True

#
# encrypt strings using polymorphic encryption algorithms
#
myAutoItObfuscator.cryptStrings = True

#
# insert ternary operators for numerical values
#
myAutoItObfuscator.insertTernaryOperators = True

#
# source code in AutoIt v3 format
#
scriptSourceCode = 'ConsoleWrite("Hello World")'

#
# by default all options are enabled, both helper random numbers
# generation & obfuscation strategies, so we can just simply call:
#
result = myAutoItObfuscator.obfuscate_script_source(scriptSourceCode)

#
# result[] array holds the obfuscation results as well as other information
#
# result["error"]         - error code
# result["output"]        - obfuscated code
# result["demo"]          - was it used in demo mode (invalid or empty activation key was used)
# result["credits_left"]  - usage credits left after this operation
# result["credits_total"] - total number of credits for this activation code
# result["expired"]       - if this was the last usage credit for the activation key it will be set to True
#
if result and "error" in result:

	# display obfuscated code
	if result["error"] == AutoItObfuscator.ERROR_SUCCESS:

		# format output code for HTML display
		print(result["output"])
	else:
		print(f'An error occurred, error code: {result["error"]}')

else:
	print("Something unexpected happen while trying to obfuscate the code.")
