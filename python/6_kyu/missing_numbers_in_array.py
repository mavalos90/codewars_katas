# Unknown Amount of Missing Numbers in an Unordered Array
# 6 kyu

'''
We have a big list having values fom 1 to n, occurring only once but unordered with an unknown amount of missing values. The number n will be considered the maximum value of the array.

We have to output the missing numbers sorted by value. Example:

[8, 10, 11, 7, 3, 15, 6, 1, 14, 5, 12]  ---> [2, 4, 9, 13]
The number 1 should be in the input array, if it's not present in the input array, should be included in the results. See the example below.

[8, 10, 11, 7, 3, 15, 6, 14, 5, 12]  ---> [1, 2, 4, 9, 13]
As this is a hardcore version, the tests are prepared for only algorithms of time complexityO(n) to pass. As the speed of each language are different, we will have different maximum lengths for the input.

Features of the random tests:
1000 <= length of arrays <= 4.000.000 (Python)
1000 <= length of arrays <= 14.000.000 (Ruby)
1000 <= length of arrays <= 30.000.000 (Javascript)
1 <= amount of missing numbers <= 10
amount of tests: 20
'''

def miss_nums_finder(arr):
    s = set(arr)
    return [x for x in range(1, max(arr) + 1) if x not in s]
	
# Alternative:

def miss_nums_finder(arr):
    n_range = set(range(1, (max(arr)+1))) 
    missing  = list(n_range - set(arr)) 
    return  sorted(missing)
