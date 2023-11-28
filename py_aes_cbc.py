#!/usr/bin/env python3
#
# This is a simple script to encrypt a message using AES
# with CBC mode in Python 3.
# Before running it, you must install pycryptodome:
#
# $ python -m pip install PyCryptodome
#
# Author.: Chad Rosenbohm
# Date...: 2023-01-25
##

from binascii import hexlify, unhexlify
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import sys

class AESCipher:

    def __init__(self, key):
        self.key=unhexlify(key)

    def encrypt(self, data):
        iv=bytearray(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.cipher.encrypt(pad(unhexlify(data), AES.block_size)).hex()

    def decrypt(self, data):
        raw=unhexlify(data)
        iv=bytearray(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(self.cipher.decrypt(raw), AES.block_size).hex()

if __name__ == '__main__':

    # set variables
    ver = sys.argv[1]
    key = sys.argv[2]
    txt = sys.argv[3]

    # encrypt or decrypt value
    if  ver == 'encrypt':
        val=AESCipher(key).encrypt(txt)
        print(val)
    else:
        val=AESCipher(key).decrypt(txt)
        print(val)
