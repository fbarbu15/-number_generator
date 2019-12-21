'''
Created on Dec 21, 2019

@author: Florin
'''
import pytest
from libs.number_generator import NumberGenerator
from resources.variables import START_A, MULTIPLY_FACTOR_A, START_B, \
    MULTIPLY_FACTOR_B


class TestsBinary():

    @pytest.fixture(scope="function", autouse=True)
    def _setup_teardown_test(self):
        self.num_gen_a = NumberGenerator(START_A, MULTIPLY_FACTOR_A)
        self.num_gen_b = NumberGenerator(START_B, MULTIPLY_FACTOR_B)

    def test_first_five_pairs(self):
        for i in range(5):
            if i == 2:
                assert self.num_gen_a.next_value(self.num_gen_a.current_value).to_binary()[-16:] == self.num_gen_b.next_value(self.num_gen_b.current_value).to_binary()[-16:], \
                    "Least significant 16 bits should've matched for the 3rd pair"
            else:
                assert self.num_gen_a.next_value(self.num_gen_a.current_value).to_binary()[-16:] != self.num_gen_b.next_value(self.num_gen_b.current_value).to_binary()[-16:], \
                    "Least significant 16 bits should match only for the 3rd pair, not here"

    def test_count_match_on_40_million_pairs(self):
        total_count = 0
        for _ in range(40000000):  # This runs in 80 seconds on my machine
            if self.num_gen_a.next_value(self.num_gen_a.current_value).to_binary()[-16:] == self.num_gen_b.next_value(self.num_gen_b.current_value).to_binary()[-16:]:
                total_count += 1
        assert total_count == 588, "Total matching pairs in 40 million rows is incorrect. Got <{0}> but expected <{1}>".format(total_count, 588)
