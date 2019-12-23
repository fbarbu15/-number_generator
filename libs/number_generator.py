'''
Created on Dec 21, 2019

@author: Florin
'''
from resources.variables import DIVIDE_FACTOR


class NumberGenerator():

    def __init__(self, start_value, multiply_factor):
        self.current_value = start_value
        self._multiply_factor = multiply_factor

    def __next__(self):
        self.current_value = (self.current_value * self._multiply_factor) % DIVIDE_FACTOR
        return self.current_value
