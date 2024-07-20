# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:47:46 2024

@author: cacha
"""

import hashlib 
import time

message = input("Provide message to hash -> ")
nonce = 0
target = '000001ab420404a0811733cfb7b190d62c65bf0bcda32b13f48462f2b8d3e5'
start_time = time.time()

while True:
    sha256_hash = hashlib.sha256()
    inputs = message + str(nonce)
    sha256_hash.update(inputs.encode('utf-8'))
    result = sha256_hash.hexdigest()

    if result <= target:
        nonce1 = "{:,}".format(nonce)
        print(f'\nHash: {result}, \nNonce: {nonce1}')
        end_time = time.time()
        break
    nonce += 1

totaltime = end_time - start_time
print(f"Time taken: {totaltime:.2f} seconds")

hashrate = nonce / totaltime
hashrate = "{:,}".format(hashrate)
print(f'Hashrate: {hashrate}')