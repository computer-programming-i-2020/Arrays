'''
Created on Jul 23, 2019

@author: karl
'''

# Arrays hold multiple values of the same data type

# Examples on creating arrays
myArray1 = [0, 1, 3, 4]
myArray2 = ["abc", "def", "ghi"]

# Arrays can be used as one unit
print(myArray1)

# You can also use specific values stored in an array
print(myArray2[1])  # Square Brackets following the array can be used to specify the index inside the array that you are referring to
                    # Array indexes start at 0
                    
# There are also procedures that can be used to change the values in an array
myArray1.insert(1, 4)   # The first parameter is used to specify the index of where you are placing the new value, which is the second parameter
myArray1.append(5)      # This adds a value to the next unused index in an array
print(myArray1)
myArray2.reverse()      # Reverses the order of each object in the array
myArray2.remove("abc")  # Removes the first object in the array with the same value as the parameter
print(myArray2)
myArray2.clear()        # This will clear all of the objects from the array
print(myArray2)

# Arrays contain functions that can be used to return information about them
print(myArray1.__len__())   # Returns the number of objects in the array
print(myArray1.count(4))    # Returns the number of objects with the value of the parameter in the array
print(myArray1.index(3))    # Returns the index of the first object in the array with the value of the parameter