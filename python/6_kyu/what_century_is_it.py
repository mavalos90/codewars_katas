# What century is it?
# 6 kyu

'''
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
'''

def what_century(year):
    century = str(((int(year) - 1) // 100) + 1)
    if century[-1] == '1' and century[-2] != '1': 
		century += 'st'
    elif century[-1] == '2' and century[-2] != '1': 
		century += 'nd'
    elif century[-1] == '3' and century[-2] != '1': 
		century += 'rd'
    else: 
		century += 'th'
    return century