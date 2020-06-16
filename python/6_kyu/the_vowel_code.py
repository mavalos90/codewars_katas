# The Vowel Code
# 6 kyu

'''
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
'''

VOWELS = ['a', 'e', 'i', 'o', 'u']

def encode(st):
    r = ''
    for char in st:
        if char in VOWELS:
            r += str(VOWELS.index(char) + 1)
        else: r += char
    return r
    
def decode(st):
    r = ''
    for char in st:
        if char.isdigit():
            r += str(VOWELS[int(char) - 1])
        else: r += char
    return r

	
# Alternative solution

def encode(st):
    t=str.maketrans("aeiou", "12345")
    return st.translate(t)
    
def decode(st):
    t=str.maketrans("12345", "aeiou")
    return st.translate(t)