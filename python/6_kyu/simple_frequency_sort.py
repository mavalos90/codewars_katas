# Simple frequency sort
# 6 kyu

'''
In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
--we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
More examples in test cases.

Good luck!
'''

def solve(arr):
    counts = [(n, arr.count(n)) for n in set(arr)]
    counts.sort(key=lambda tup: (-tup[1], tup[0]))
    result = []
    for i, j in counts:
        result += ([i] * j)
    return result
	
# One line solution:

def solve(arr):
    return sorted(arr, key= lambda x: (-arr.count(x), x))