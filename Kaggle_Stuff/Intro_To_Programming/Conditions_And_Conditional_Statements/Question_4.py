# TODO: Edit the function to return the correct bill for different
# values of GB
from learntools.core import binder

binder.bind(globals())
from learntools.intro_to_programming.ex4 import *

print('Setup complete.')


def get_phone_bill(gb):
    base_cost = 100

    included_data = 15.0
    cost_per_mb = 0.10

    if data_usage <= included_data:
        return base_cost
    else:
        overage_gb = gb - included_data
        overage_mb = overage_gb * 1000

        overage_cost = overage_mb * cost_per_mb

        total_cost = base_cost + overage_cost

        return total_cost


# Check your answer
q4.check()