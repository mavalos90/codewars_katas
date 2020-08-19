# The Deaf Rats of Hamelin
# 6kyu

'''
Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats
ex2 P O~ O~ ~O O~ has 1 deaf rat
ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
'''

def count_deaf_rats(town):
    deaf = 0
    
    # Get position of the Piper
    left = town.split('P')[0].replace(' ', '')
    right = town.split('P')[1].replace(' ', '')
    
    # Get list of rats
    l = [left[i:i+2] for i in range(0, len(left), 2)]
    r = [right[i:i+2] for i in range(0, len(right), 2)]
        
    # Count deaf rats
    for rat in l:
        if rat == 'O~': deaf += 1
    for rat in r:
        if rat == '~O': deaf += 1

    return deaf 