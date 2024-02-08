#!/usr/bin/env python

###############################################################################
#
# AutoIt Obfuscator Web API interface can help you to protect your AutoIt
# script source code against analysis, reverse engineering and
# decompilation.
#
# AutoIt Obfuscator provides advanced AutoIt source code parsing based
# on AST trees, multiple advanced obfuscation strategies are available.
#
# Version      : AutoItObfuscator v1.04
# Python       : Python v3
# Dependencies : requests (https://pypi.python.org/pypi/requests/)
# Author       : Bartosz Wójcik (support@pelock.com)
# Project      : https://www.pelock.com/products/autoit-obfuscator
# Homepage     : https://www.pelock.com
#
###############################################################################

import zlib
import base64

# required external package - install with "pip install requests"
import requests

class AutoItObfuscator(object):
    """AutoIt Obfuscator module"""

    # 
    # @var string default AutoIt Obfuscator WebApi endpoint
    # 
    API_URL = "https://www.pelock.com/api/autoit-obfuscator/v1"

    # 
    # @var string WebApi key for the service
    # 
    _apiKey = ""

    # 
    # @var bool should the source code be compressed
    # 
    enableCompression = False

    #
    # @var bool detect debuggers attached to the application process
    #
    antiDebug = False

    #
    # @var bool detect popular virtual machines
    #
    antiVM = False

    #
    # @var bool detect sandboxes
    #
    antiSandbox = False

    #
    # @var bool detect CPU emulators
    #
    antiEmulator = False

    #
    # @var bool generate random integer values
    # 
    randomIntegers = False

    # 
    # @var bool generate random value characters
    # 
    randomCharacters = False

    # 
    # @var bool generate random anti regular expression values
    # 
    randomAntiRegex = False

    # 
    # @var bool generate arrays with random values
    # 
    randomArrays = False

    # 
    # @var bool generate multidimensional arrays with random values
    # 
    randomArraysMultidimensional = False

    # 
    # @var bool generate functions that returns random values
    # 
    randomFunctions = False

    # 
    # @var bool generate autostarted random values
    # 
    randomAutostarted = False

    # 
    # @var bool change linear code execution flow to nonlinear version
    # 
    mixCodeFlow = False

    # 
    # @var bool rename variable names to random string values
    # 
    renameVariables = False

    # 
    # @var bool rename function names to random string values
    # 
    renameFunctions = False

    # 
    # @var bool rename function names in function calls
    # 
    renameFunctionCalls = False

    # 
    # @var bool shuffle functions order in the output source
    # 
    shuffleFunctions = False

    # 
    # @var bool resolve WinApi constants to numerical values
    # 
    resolveConstants = False

    # 
    # @var bool encrypt numbers into arithmetic and boolean expressions
    # 
    cryptNumbers = False

    # 
    # @var bool split strings into series of random sized substrings
    # 
    splitStrings = False

    # 
    # @var bool modify strings using built-it AutoIt string functions
    # 
    modifyStrings = False

    # 
    # @var bool encrypt strings using polymorphic encryption algorithms
    # 
    cryptStrings = False

    # 
    # @var bool insert ternary operators for numerical values
    # 
    insertTernaryOperators = False

    # 
    # @var integer success
    # 
    ERROR_SUCCESS = 0

    # 
    # @var integer invalid size for source code (it's 1000 bytes max. for demo version)
    # 
    ERROR_INPUT_SIZE = 1

    # 
    # @var integer input source is empty
    # 
    ERROR_INPUT = 2

    # 
    # @var integer AutoIt source code parsing error
    # 
    ERROR_PARSING = 3

    # 
    # @var integer AutoIt parsed code obfuscation error
    # 
    ERROR_OBFUSCATION = 4

    # 
    # @var integer AutoIt error while generating output code
    # 
    ERROR_OUTPUT = 5

    def __init__(self, api_key=None, enable_all_obfuscation_options=True):
        """Initialize AutoItObfuscator class

        :param api_key: Activation key for the service (it can be empty for demo mode)
        :param enable_all_obfuscation_options: Enable or disable all of the obfuscation options
        """

        self._apiKey = api_key
        
        self.enableCompression = enable_all_obfuscation_options

        self.antiDebug = enable_all_obfuscation_options
        self.antiVM = enable_all_obfuscation_options
        self.antiSandbox = enable_all_obfuscation_options
        self.antiEmulator = enable_all_obfuscation_options

        self.randomIntegers = enable_all_obfuscation_options
        self.randomCharacters = enable_all_obfuscation_options
        self.randomAntiRegex = enable_all_obfuscation_options
        self.randomArrays = enable_all_obfuscation_options
        self.randomArraysMultidimensional = enable_all_obfuscation_options
        self.randomFunctions = enable_all_obfuscation_options
        self.randomAutostarted = enable_all_obfuscation_options
        self.mixCodeFlow = enable_all_obfuscation_options
        self.renameVariables = enable_all_obfuscation_options
        self.renameFunctions = enable_all_obfuscation_options
        self.renameFunctionCalls = enable_all_obfuscation_options
        self.shuffleFunctions = enable_all_obfuscation_options
        self.resolveConstants = enable_all_obfuscation_options
        self.cryptNumbers = enable_all_obfuscation_options
        self.splitStrings = enable_all_obfuscation_options
        self.modifyStrings = enable_all_obfuscation_options
        self.cryptStrings = enable_all_obfuscation_options
        self.insertTernaryOperators = enable_all_obfuscation_options

    def login(self):
        """Login to the service and get the information about the current license limits

        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        # parameters
        params = {"command": "login"}

        return self.post_request(params)

    def obfuscate_script_file(self, script_script_file_path):
        """Obfuscate AutoIt script source code using provided parameters

        :param script_script_file_path: AutoIt compatible script *.au3 file path
        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        source_file = open(script_script_file_path, 'r')
        source = source_file.read()
        source_file.close()
    
        if not source:
            return False
    
        return self.obfuscate_script_source(source)

    def obfuscate_script_source(self, script_source):
        """Obfuscate AutoIt script source code using provided parameters

        :param script_source: AutoIt compatible script *.au3 source code
        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        # additional parameters
        params_array = {"command": "obfuscate", "source": script_source}

        return self.post_request(params_array)

    def post_request(self, params_array):
        """Send a POST request to the server

        :param params_array: An array with the parameters
        :param return_as_array: Return result as an associative array or JSON encoded string
        :return: An array with the results or false on error
        :rtype: bool,dict
        """

        # add activation key to the parameters array
        if self._apiKey: params_array["key"] = self._apiKey

        #
        # detections
        #
        if self.antiDebug: params_array["anti_debug"] = "1"
        if self.antiVM: params_array["anti_vm"] = "1"
        if self.antiSandbox: params_array["anti_sandbox"] = "1"
        if self.antiEmulator: params_array["anti_emulator"] = "1"

        #
        # random bucket setup
        #
        if self.randomIntegers: params_array["random_bucket_integers"] = "1"
        if self.randomCharacters: params_array["random_bucket_characters"] = "1"
        if self.randomAntiRegex: params_array["random_bucket_anti_regex"] = "1"
        if self.randomArrays: params_array["random_bucket_arrays"] = "1"
        if self.randomArraysMultidimensional: params_array["random_bucket_arrays_multidimensional"] = "1"
        if self.randomFunctions: params_array["random_bucket_functions"] = "1"
        if self.randomAutostarted: params_array["random_bucket_autostart"] = "1"

        #
        # obfuscation strategies
        #
        if self.mixCodeFlow: params_array["mix_code_flow"] = "1"
        if self.renameVariables: params_array["rename_variables"] = "1"
        if self.renameFunctions: params_array["rename_functions"] = "1"
        if self.renameFunctionCalls: params_array["rename_function_calls"] = "1"
        if self.shuffleFunctions: params_array["shuffle_functions"] = "1"
        if self.resolveConstants: params_array["resolve_const"] = "1"
        if self.cryptNumbers: params_array["crypt_numbers"] = "1"
        if self.splitStrings: params_array["split_strings"] = "1"
        if self.modifyStrings: params_array["modify_strings"] = "1"
        if self.cryptStrings: params_array["crypt_strings"] = "1"
        if self.insertTernaryOperators: params_array["insert_ternary_operators"] = "1"

        #
        # check if compression is enabled
        #
        if "source" in params_array and self.enableCompression and params_array["source"]:

            compressed_data = zlib.compress(bytes(params_array["source"], 'utf-8'), 9)
            base64_encoded_data = base64.b64encode(compressed_data).decode()

            params_array["source"] = base64_encoded_data
            params_array["compression"] = "1"

        response = requests.post(self.API_URL, data=params_array)

        # no response at all or an invalid response code
        if not response or not response.ok:
            return False

        # decode to json array
        result = response.json()

        # depack output code back into the string
        if "output" in result and self.enableCompression and result["error"] == self.ERROR_SUCCESS:

            result["output"] = str(zlib.decompress(base64.b64decode(result["output"])), "utf-8")

        # return original JSON response code
        return result
