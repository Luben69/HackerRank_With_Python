import math
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex2 import *
print('Setup complete.')
# TODO: Complete the function
def get_expected_cost(beds, baths):
    value = 80000 + (beds * 30000) + (baths * 10000)
    return value

# Check your answer
q1.check()