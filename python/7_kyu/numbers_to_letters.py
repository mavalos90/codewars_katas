# Numbers to Letters
# 7 kyu

'''
Given an array of numbers (in string format), you must return a string. The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

All inputs will be valid.
'''


def switcher(arr):
    special = {27: '!', 28: '?', 29: ' '}
    s = ''
    for n in arr:
        if int(n) <= 26:
            s += chr(123 - int(n))
        else:
            s += special[int(n)]
    return s