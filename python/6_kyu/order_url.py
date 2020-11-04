# "com", "gov", "org" first
# 6 kyu

'''
Write a code that orders collection of Uris based on it's domain next way that it will returns fisrt Uris with domain "com", "gov", "org" (in alphabetical order of their domains) and then all other Uris ordered in alphabetical order of their domains In addition to that

content of Uri should not be changed,
other part of Uri doesn't affect sorting. (uris "c.com","b.com","a.com" can be placed in any order inside their group, so both "c.com","b.com","a.com" and "a.com","c.com","b.com" are correct, till they are stand before *.org)
e.g.

"http://www.google.en/?x=jsdfkj"
"http://www.google.de/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.org/?x=jsdfkj"
"http://www.google.gov/?x=jsdfkj"
should be sorted into

"http://www.google.com/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.gov/?x=jsdfkj"
"http://www.google.org/?x=jsdfkj"
"http://www.google.de/?x=jsdfkj"
"http://www.google.en/?x=jsdfkj"
In the final tests consecutive addresses with the same domain will be grouped and sorted before comparison, i.e.:

Given your solution returns ["b.com", "a.com", "c.gov"], the tests will do this:

Split the addresses into groups: [["b.com", "a.com"], ["c.gov"]]
Sort each group: [["a.com", "b.com"], ["c.gov"]]
Flatten them: ["a.com", "b.com", "c.gov"]
'''

def order_by_domain(addresses):
    com = [url for url in addresses if '.com' in url]
    gov = [url for url in addresses if '.gov' in url and url not in com]
    org = [url for url in addresses if '.org' in url and url not in (com + gov)]
    other = [(url.split('/')[2].split('.')[-1], url)  for url in addresses if url not in (com + gov + org)]
    oth = [tupl[1] for tupl in sorted(other)]
    return sorted(com) + sorted(gov) + sorted(org) + oth