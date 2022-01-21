"""
Mental math practice program, intended to be used to practice the techniques
described in "The Secrets of Mental Math" by Arthur Benjamin

P.S. Pep8 line length limit is 79 characters
"""
import math
import numpy as np


while True:

    print("Push a key")
    user_key = input()

    print(user_key)

    if user_key.lower() == 'q':
        break


print("Loop is exited")