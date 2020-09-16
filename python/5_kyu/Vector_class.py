# Vector class
# 5 kyu

'''
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
'''

import math

class Vector:
    def __init__(self, vec):
        self.vec = vec
        self.len = len(vec)

    def add(self, vec):
        if self.len == vec.len:
            return Vector([x+y for x,y in zip(self.vec, vec.vec)])

    def subtract(self, vec):
        if self.len == vec.len:
            return Vector([x-y for x,y in zip(self.vec, vec.vec)])

    def dot(self, vec):
        if self.len == vec.len:
            return sum([x*y for x,y in zip(self.vec, vec.vec)])

    def norm(self):
        vecsquared = [x**2 for x in self.vec]
        return math.sqrt(sum(vecsquared))

    def __str__(self):
        return str(tuple(self.vec)).replace(' ', '')

    def equals(self, vec):
        return self.vec == vec.vec