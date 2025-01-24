import math
from learntools.core import binder

binder.bind(globals())
from learntools.intro_to_programming.ex2 import *

print('Setup complete.')


# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_area = sqft_walls + sqft_ceiling

    # Calculate the gallons of paint needed
    gallons_needed = total_area / sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost


# Check your answer
q3.check()