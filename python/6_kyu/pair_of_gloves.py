# Pair of gloves
# 6 kyu

'''
Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.
A pair of gloves is constituted of two gloves of the same color.
You are given an array containing the color of each glove.
You must return the number of pair you can constitute.
You must not change the input array.

Example :
my_gloves = ["red","green","red","blue","blue"]
number_of_pairs(my_gloves) == 2;// red and blue

red_gloves = ["red","red","red","red","red","red"];
number_of_pairs(red_gloves) == 3; // 3 red pairs
'''

def number_of_pairs(gloves):
    count = 0
    for color in set(gloves):
        count += gloves.count(color) // 2
    return count

# One line solution:	
def number_of_pairs(gloves):
	return sum(gloves.count(color) // 2 for color in set(gloves))