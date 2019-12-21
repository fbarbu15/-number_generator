'''
Created on Dec 21, 2019

@author: Florin
'''
from resources.variables import DIVIDE_FACTOR


class NumberGenerator():

    def __init__(self, start_value, multiply_factor):
        self.current_value = start_value
        self._multiply_factor = multiply_factor

    def next_value(self, previous_value):
        self.current_value = (previous_value * self._multiply_factor) % DIVIDE_FACTOR
        return self

    def to_binary(self):
        return bin(self.current_value)
