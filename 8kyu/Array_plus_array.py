#Array plus array

"""
DESCRIPTION:
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
"""

def array_plus_array(arr1,arr2):
    arr3 = arr1 + arr2
    sum = 0
    for i in arr3:
        sum += i
    return sum
