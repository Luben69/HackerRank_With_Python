# TODO: Edit the function to return the correct bill for different
from learntools.core import binder

binder.bind(globals())
from learntools.intro_to_programming.ex4 import *

print('Setup complete.')


# values of num_gallons
def get_water_bill(num_gallons):
    if 0 <= num_gallons <= 8_000:
        bill = 5 * (num_gallons / 1_000)

    elif 8_001 <= num_gallons <= 22_000:
        bill = 6 * (num_gallons / 1_000)

    elif 22_001 <= num_gallons <= 30_000:
        bill = 7 * (num_gallons / 1_000)

    else:
        bill = 10 * (num_gallons / 1_000)

    return bill


# Check your answer
q3.check()