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
# source code in AutoIt v3 format
#
scriptSourceCode = 'ConsoleWrite("Hello World")'

#
# by default all options are enabled, both helper random numbers
# generation & obfuscation strategies, so we can just simply call:
#
result = myAutoItObfuscator.obfuscate_script_source(scriptSourceCode)

#
# it's also possible to pass script path instead of a string with the source e.g.
#
# result = myAutoItObfuscator.obfuscate_script_file("/path/to/script/source.au3")

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
