# Responsible Drinking
# 7 kyu

'''
Welcome to the Codewars Bar!
Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.

Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.

Examples
"1 beer"  =>  "1 glass of water"
"1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water"
'''

import re
def hydrate(drink_string): 
    drinks = re.findall(r'\d+', drink_string)
    total = sum(map(int, drinks))
    return "1 glass of water" if total == 1 else str(total) + " glasses of water"