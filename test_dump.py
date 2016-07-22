 # -*- coding:utf-8 -*-

from __future__ import print_function
import sys
import chardet
import binascii
import struct

"""
http://www.lifewithpython.com/2013/12/python-print-without-.html
"""
with open(sys.argv[1], "rb") as f:
    print("HEX")
    i = 0
    while 1:
        b = f.read(1)
        if b == "":
            break
        print(binascii.b2a_hex(b),end='')
        if ((i+1) % 16) == 0:
            print("")
        i = i + 1
        
