from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex1 import *
print('Setup complete.')
# TODO: Set the value of the births_per_min variable
births_per_min = 250

# TODO: Set the value of the births_per_day variable
births_per_day = births_per_min * (24 * 60)

# DO NOT REMOVE: Check your answer
q4.check()