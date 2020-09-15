# Count IP Addresses
# 5 kyu

'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50 
ips_between("10.0.0.0", "10.0.1.0")   ==  256 
ips_between("20.0.0.10", "20.0.1.0")  ==  246
'''


def ips_between(start, end):
    s1, s2, s3, s4 = start.split('.')
    e1, e2, e3, e4 = end.split('.')
    return ((int(e1) - int(s1)) * 256 ** 3) + ((int(e2) - int(s2)) * 256 ** 2) + ((int(e3) - int(s3)) * 256) + (int(e4) - int(s4))