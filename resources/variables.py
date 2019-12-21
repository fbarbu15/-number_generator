'''
Created on Dec 21, 2019

@author: Florin
'''

import os

# Start A and B can be passed as environment variables (from CI build params for example)
START_A = os.getenv("START_A", 65)
START_B = os.getenv("START_B", 8921)

MULTIPLY_FACTOR_A = 16807
MULTIPLY_FACTOR_B = 48271

DIVIDE_FACTOR = 2147483647
