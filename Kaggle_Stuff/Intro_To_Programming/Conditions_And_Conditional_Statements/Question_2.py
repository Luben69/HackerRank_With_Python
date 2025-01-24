from learntools.core import binder

binder.bind(globals())
from learntools.intro_to_programming.ex4 import *

print('Setup complete.')


def cost_of_project(engraving, solid_gold):
    enr_len = len(engraving)

    if solid_gold == True:
        cost = 100 + (enr_len * 10)
    else:
        cost = 50 + (enr_len * 7)
    return cost


# Check your answer
q2.check()