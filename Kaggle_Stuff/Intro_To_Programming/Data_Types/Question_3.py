# TODO: Complete the function
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex3 import *
print('Setup complete.')
def get_expected_cost(beds, baths, has_basement):
    value = 80000 + int(beds * 30000) + int(baths * 10000)
    if has_basement:
        value += 40000
    return value

# Check your answer
q3.check()