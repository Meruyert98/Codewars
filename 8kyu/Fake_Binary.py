#Fake Binary

"""
DESCRIPTION:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""

def fake_bin(x):
    arr = list(x)
    l = ''
    for i in arr:
        if int(i) >= 5:
            l += '1'
        else:
            l += '0'
    return l
