# TODO: Edit the function to return the correct grade for different scores
from learntools.core import binder

binder.bind(globals())
from learntools.intro_to_programming.ex4 import *

print('Setup complete.')


def get_grade(score):
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"
    return grade


# Check your answer
q1.check()