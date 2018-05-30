import os, random, struct
from Crypto.Cipher import AES
from simplecrypt import encrypt, decrypt
import asyncio


#################################################################################
async def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + '.enc'
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            while True:
                print('.')
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                else:
                    text = encrypt(key,chunk)
                outfile.write(text)

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    pass