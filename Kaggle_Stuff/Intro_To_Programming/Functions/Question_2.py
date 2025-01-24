import math
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex2 import *
print('Setup complete.')
# TODO: Use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2, 3)
option_two = 80000 + get_expected_cost(3, 2)
option_three = 80000 + get_expected_cost(3, 3)
option_four = 80000 + get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Check your answer
q2.check()