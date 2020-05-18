#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen) :
    #
    #
    letters = string.ascii_lowercase
    #
    #
    return "".join(random.choice(letters) for i in range(passLen))


print(RandomPasswordGenerator(100)) 
    
