# Alien Beer Morse Code
# 6 kyu

'''
The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply the exact number of beers demanded.

Unfortunately, the aliens only speak Morse code. Write a program to convert morse code into numbers using the following convention:

1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----
'''

import re
def morse_converter(string):
    code = {'.----': 1, '..---': 2, '...--': 3, '....-': 4, '.....': 5,
           '-....': 6, '--...': 7, '---..': 8, '----.': 9, '-----': 0}
    chunks = re.findall('.{5}', string)
    result = ''
    for c in chunks:
        if c in code.keys():
            result += str(code[c])
    return int(result)
	
