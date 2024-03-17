#!/usr/bin/env python3

""" Test env """


from dotenv import load_dotenv
from os import getenv

load_dotenv()

key = getenv('KEY')

print(key)