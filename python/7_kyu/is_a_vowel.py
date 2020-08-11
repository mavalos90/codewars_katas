# Regexp Basics - is it a vowel?
# 7 kyu

# Implement the function which should return true if given object is a vowel (meaning a, e, i, o, u), and false otherwise.

def is_vowel(s): 
    vowels = ['a','e','i','o','u']
    return s.lower() in vowels