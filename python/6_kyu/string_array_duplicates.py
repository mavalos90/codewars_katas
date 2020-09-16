# String array duplicates
# 6 kyu

'''
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.
For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be alphabet characters only. Don't worry about lower and upper case. See test cases for more examples.
Good luck!
'''

def dup(arry):
    r = []
    for word in arry:
        w = word[0]
        for i in word:
            if i != w[-1]:
                w += i
        r.append(w)
    return r