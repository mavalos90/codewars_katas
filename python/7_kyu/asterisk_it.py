# Asterisk it
# 7 kyu

'''
Task
You are given a function that should insert an asterisk (*) between every pair of even digits in the given input, and return it as a string. If the input is a sequence, concat the elements first as a string.

Input
The input can be an integer, a string of digits or a sequence containing integers only.

Output
Return a string.

Examples
5312708     -->  "531270*8"
"0000"      -->  "0*0*0*0"
[1, 4, 64]  -->  "14*6*4"
'''

def asterisc_it(n):
    
    if type(n) is list:
        x = ''.join(map(str, n))
    else:
        x=str(n)
    r = ''
    for i in range(len(x)-1):
        if int(x[i])%2==0 and int(x[i+1])%2==0:
            r += x[i]+'*'
        else:
            r += x[i]
    r += x[len(x)-1]
    return r