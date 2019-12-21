'''
Created on Dec 21, 2019

@author: Florin
'''
import pytest
from libs.number_generator import NumberGenerator
from resources.variables import MULTIPLY_FACTOR_A, MULTIPLY_FACTOR_B


class TestsFirstFive():

    @pytest.fixture(scope="function", autouse=True)
    def _setup_teardown_test(self):
        self.first_five_values = []

    def test_generator_a(self):
        num_gen_a = NumberGenerator(65, MULTIPLY_FACTOR_A)
        for _ in range(5):
            self.first_five_values.append(num_gen_a.next_value(num_gen_a.current_value).current_value)
        assert self.first_five_values[0] == 1092455, "First value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[0], 1092455)
        assert self.first_five_values[1] == 1181022009, "Second value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[1], 1181022009)
        assert self.first_five_values[2] == 245556042, "Third value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[2], 245556042)
        assert self.first_five_values[3] == 1744312007, "Fourth value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[3], 1744312007)
        assert self.first_five_values[4] == 1352636452, "Fifth value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[4], 1352636452)

    def test_generator_b(self):
        num_gen_b = NumberGenerator(8921, MULTIPLY_FACTOR_B)
        for _ in range(5):
            self.first_five_values.append(num_gen_b.next_value(num_gen_b.current_value).current_value)
        assert self.first_five_values[0] == 430625591, "First value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[0], 430625591)
        assert self.first_five_values[1] == 1233683848, "Second value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[1], 1233683848)
        assert self.first_five_values[2] == 1431495498, "Third value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[2], 1431495498)
        assert self.first_five_values[3] == 137874439, "Fourth value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[3], 137874439)
        assert self.first_five_values[4] == 285222916, "Fifth value not generated correctly. Got <{0}> but expected <{1}>".format(self.first_five_values[4], 285222916)
