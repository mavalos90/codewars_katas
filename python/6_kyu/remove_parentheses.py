# Remove the parentheses
# 6 kyu

'''
Remove the parentheses
In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"
Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
'''

def remove_parentheses(s):
    result = ''
    level = 0
    for ch in s:
        if ch == '(':
            level += 1
        elif (ch == ')') and level:
            level -= 1
        elif not level:
            result += ch
    return result