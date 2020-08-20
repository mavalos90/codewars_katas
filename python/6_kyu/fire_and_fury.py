# FIRE and FURY
# 6 kyu

'''
The President's phone is broken
He is not very happy.
The only letters still working are uppercase E, F, I, R, U, Y.
An angry tweet is sent to the department responsible for presidential phone maintenance.

Kata Task
Decipher the tweet by looking for words with known meanings.

FIRE = *"You are fired!"*
FURY = *"I am furious."*
If no known words are found, or unexpected letters are encountered, then it must be a *"Fake tweet."*

Notes
The tweet reads left-to-right.
Any letters not spelling words FIRE or FURY are just ignored
If multiple of the same words are found in a row then plural rules apply -
FIRE x 1 = *"You are fired!"*
FIRE x 2 = *"You and you are fired!"*
FIRE x 3 = *"You and you and you are fired!"*
etc...
FURY x 1 = *"I am furious."*
FURY x 2 = *"I am really furious."*
FURY x 3 = *"I am really really furious."*
etc...
Examples
ex1. FURYYYFIREYYFIRE = *"I am furious. You and you are fired!"*
ex2. FIREYYFURYYFURYYFURRYFIRE = *"You are fired! I am really furious. You are fired!"*
ex3. FYRYFIRUFIRUFURE = *"Fake tweet."*
'''

import re
from itertools import groupby

def fire_and_fury(tweet):
	
	# Check fake cases
    letters = ['E', 'F', 'I', 'R', 'U', 'Y']
    for i in tweet:
        if i not in letters:
            return "Fake tweet."
    words = re.findall(r'(FURY|FIRE)', tweet)
    if len(words) == 0:    
        return "Fake tweet."
    
	# Count how many times a word appears consecutively
    unique = [x[0] for x in groupby(words)]
    count_dups = [sum(1 for x in group) for x, group in groupby(words)]
    code = zip(unique, count_dups)
    
	# Translate the code
    result = ''
    for i in code:
        if i[0] == 'FURY':
            result += 'I am ' + str('really ' * (i[1] - 1)) + 'furious. '
        else:
            result += 'You ' + str('and you ' * (i[1] -1)) + 'are fired! '
    return result[:-1]
