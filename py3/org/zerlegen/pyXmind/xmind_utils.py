#!/usr/bin/python3

################################################################################
# Misc utils for dealing with XMind mind maps
################################################################################


import time
import binascii
import random

def generate_xmind_timestamp():
	return (str(int(time.time()) * 1000))

def generate_object_id():
    # XMind ids are a 26-char hex string
    return bytes.decode(binascii.hexlify(random._urandom(13)))


