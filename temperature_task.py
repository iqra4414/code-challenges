# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:10:12 2022

@author: PERSONAL
"""

fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

# Get the corresponding `celsius` values in list
celsius = list(map(lambda x:(float(5)/9)*(x-32), fahrenheit.values()))

# Create the `celsius` dictionary
celsius_dict=dict(zip(fahrenheit.keys(),celsius))
print(celsius_dict)
# convert a dictionary of Fahrenheit temperatures into celsius
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)

