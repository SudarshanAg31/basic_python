#module: a file containing code yo want to include in your program \
#       use 'import' to include a module(built-  in or your own)
#       useful to break up a large pragram reusable separate files

#import math
#print(math.e)
#import math as m #(we can rename as we want)
#print(m.e)
#from math import e
#print(e)
#NOTE: this are pre define module

#this module is not pre-define
import module_example
print(module_example.pi)
print(module_example.circumference(3))
print(module_example.area(3))
print(module_example.cube(3))
print(module_example.square(3))

