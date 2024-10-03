#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:43:25 2024

@author: simon

HMAC SHA-256 encryption

Generate a random secret key
Take the plaintext, convert it to binary, XOR each bit with the secret key,
hash it using hashlib documentation

---
https://docs.python.org/3/library/hashlib.html
import hashlib
hashlib.sha256(variable).hexdigest()
---
"""

import hashlib
import random

plaintext = "Hello Bob"
list_of_plaintext_characters = list(plaintext)
secretkey = []
plaintextlength = len(list_of_plaintext_characters)
counter = 0
ciphertext = []
bitlength = 7

# This will generate a random secret key for each byte
secretkey = [random.randint(0, 1) for _ in range(bitlength)]
# Converting the list of plaintext characters into binary
for char in list_of_plaintext_characters:
    binary = format(ord(char), '07b')
    digitlist = [int(digit) for digit in binary]
    # List of XOR outcomes
    xor_bits = []
    # For each bit in a byte, XOR it with secret key, and append it to ciphertext
    
    for i in range(bitlength):
        xor_result = digitlist[i] ^ secretkey[i] 
        xor_bits.append(xor_result)
        
        # This will make the binary string
    byte = int(''.join(map(str, xor_bits)), 2)
    ciphertext.append(byte)

# ciphertext needs to be readable for hashlib to compute it
cipher_list_of_bytes = bytes(ciphertext)


finalhash = hashlib.sha256(cipher_list_of_bytes).hexdigest()

print(finalhash)


        
        
    
