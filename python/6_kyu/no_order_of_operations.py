# No order of operations
# 6 kyu

'''
Imagine if there were no order of operations. Instead, you would do the problem from left to right. For example, the equation a +b *c /da+b∗c/d would become (((a+b)*c)//d)(((a+b)∗c)//d) (Math.floor(((a+b)*c)/d) in JS). Return None/null (depending on your language) if the equation is "".

Task:
Given an equation with a random amount of spaces greater than or equal to zero between each number and operation, return the result without order of operations. Note that if two numbers are spaces apart, act as if they were one number: 1 3 = 13. However, if given something % 0 or something / 0, return None/null.

More about order of operations: here

Key:
^ represents **
/ represents // or math.floor because the result will always be an integer
Operations allowed:
+, -, * , /, ^, %

Example:
no_order(2 + 3 - 4 * 1 ^ 3) returns 1
'''


import re
def no_order(equation):        
    # Delete blank spaces
    equation = equation.replace(' ', '')
    
    # Check null cases
    if '%0' in equation or '/0' in equation: 
        return None
    
    # Extract numbers and operators
    n = re.findall(r'\d+', equation)
    op = re.findall('[+\\-*/%^]', equation)
    
    #Define operators
    operators={
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
        "^": lambda x, y: x ** y,
        "%": lambda x, y: x % y}

    result = int(n[0])
    for i in range(1, len(n)):
        result = operators[op[i-1]](result, int(n[i]))
    return result