#!/usr/bin/env python3
# RyanWaltersDev Jun 29 2021
# Imports
import pizza
# Import specific function.
from pizza import make_pizza
# Import function with alias
from pizza import make_pizza as mp
# Import module with alias
import pizza as p
# Import all functions
from pizza import *

# Call from first import
pizza.make_pizza(16, 'pepperonni')
pizza.make_pizza(22, 'sausage', 'peppers', 'extra cheese')

# Call from specific import
make_pizza(16, 'pepperonni')
make_pizza(22, 'sausage', 'peppers', 'extra cheese')

# Call from import alias
mp(16, 'pepperonni')
mp(22, 'sausage', 'peppers', 'extra cheese')

# Call from module alias
p.make_pizza(16, 'pepperonni')
p.make_pizza(22, 'sausage', 'peppers', 'extra cheese')

# END OF PROGRAM
