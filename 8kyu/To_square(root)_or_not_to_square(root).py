#To square(root) or not to square(root)

"""
DESCRIPTION:
Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

Example
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
The input array will always contain only positive numbers, and will never be empty or null.
"""

def square_or_square_root(arr):
    sq = []
    for i in arr:
        sqrt_num = i**0.5
        if sqrt_num.is_integer():
            sq.append(sqrt_num)
        else:
            sq.append(i**2)
    return sq    
