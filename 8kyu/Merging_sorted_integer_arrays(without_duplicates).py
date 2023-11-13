#Merging sorted integer arrays (without duplicates)

"""
DESCRIPTION:
Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.
"""

def merge_arrays(first, second): 
    # your code here
    third = first + second
    third_lt = list(set(third))
    third_lt.sort()
    return third_lt
