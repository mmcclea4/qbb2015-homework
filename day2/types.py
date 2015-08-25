#!/usr/bin/env python

# Integer
i = 10000

# Floating point / real number
f = 0.333

# Convert integer to float
i_as_f = float(i)

# Convert float to integer
f_as_i = int(f)

# String
# "" or '' quotes define a string
s = "A String"

# Boolean
truthy = True
falsy = False

# Lists - by convention only contains one type
# [] creates lists
l = [1,2,3,4,5]
l.append(7) # lists can be changed

# Tuple - elements can have different types
# Tuples can't be changed
# () creates tuples
t = (1,"foo",5.0)

# Dictionary
d1 = { "key1": "value1", "key2": "value2" }
d2 = dict( key1="value1", key2="value2" )
d3 = dict( [ ("key1","value1"), ("key2","value2") ] ) 

for value in (i, f, s, truthy, l, t, d1, d2, d3):
    print value, type(value)
