'''
Created on Jul 23, 2019

@author: karl
'''

# Multi Dimensional Arrays are arrays that contain other arrays

# This is an example of a two dimensional array
myArray = [[1, 2], [3, 4], [5, 6]] 

# Indexes for multi dimensional arrays start at zero for each dimension
print(myArray[2][1])    # Each dimension in an array can be called using square brackets
print(myArray[0])       # Since it is an array of arrays, you can request an index from the first array to access internal arrays

# An array inside the array can be treated as a one dimensional array would
print(myArray[1].count(3))