# Strip Comments
# 4 kyu

'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''


def solution(string,markers):
    split = string.split("\n")
    result = ""
    for s in split:
        t = ""
        for char in s:
            if char not in markers:
                t += char
            else:
                break
        t = t.rstrip()
        result += t + "\n"
    return result[:-1]