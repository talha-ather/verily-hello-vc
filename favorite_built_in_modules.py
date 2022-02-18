#!/usr/bin/env python3

"""Share some of your favoriate Python built in modules!
"""

###############################################################################
#
#   Step 1. Add a line importing a module you like here.
#
#   If you aren't sure, uncoment a line below (by deleting the preceding #):
#
#import decimal
#import math
#import itertools
#import array
#import bisect
#import unittest
#import sqlite3
#
###############################################################################
import datetime
import math
import os
import array
import sqlite3

def main():
    ###########################################################################
    #
    #   Step 2. Print the module you like, and include the docstring.
    #
    ###########################################################################
    print("John DiMatteo likes datetime:", datetime.__doc__)
    print("Foo likes math:", math.__doc__)
    print("Vihang likes os and array")
    print("Foo also likes array and sqlite3")

if __name__ == "__main__":
    main()
