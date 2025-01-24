import math
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex2 import *
print('Setup complete.')
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_area = sqft_walls + sqft_ceiling
    gallons_needed = math.ceil(total_area / sqft_per_gallon)
    cost = gallons_needed * cost_per_gallon
    return cost

# Check your answer
q5.check()