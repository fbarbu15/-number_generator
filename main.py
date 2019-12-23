'''
Created on Dec 21, 2019

@author: Florin
'''
from time import time
from libs.number_generator import NumberGenerator
from resources.variables import START_A, MULTIPLY_FACTOR_A, START_B, \
    MULTIPLY_FACTOR_B

num_gen_a = NumberGenerator(START_A, MULTIPLY_FACTOR_A)
num_gen_b = NumberGenerator(START_B, MULTIPLY_FACTOR_B)

total_count = 0
start_time = time()
for _ in range(40000000):  # This runs in 80 seconds on my machine
    if bin(next(num_gen_a))[-16:] == bin(next(num_gen_b))[-16:]:
        total_count += 1

print("<{0}> matching pairs found for START A:{1} and B:{2} values. Execution time: {3} seconds".format(total_count, START_A, START_B, time() - start_time))
