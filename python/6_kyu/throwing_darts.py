# Throwing Darts
# 6 kyu

'''
You've just recently been hired to calculate scores for a Dart Board game!

Scoring specifications:

0 points - radius above 10
5 points - radius between 5 and 10 inclusive
10 points - radius less than 5
If all radii are less than 5, award 100 BONUS POINTS!

Write a function that accepts an array of radii (can be integers and/or floats), and returns a total score using the above specification.

An empty array should return 0.
'''

def score_throws(radii):
    if len(radii) == 0: return 0 #corner case
    score = 0
    low_radii = 0
    for i in radii:
        if i >= 5 and i <= 10:
            score += 5
        elif i < 5:
            score += 10
            low_radii += 1        
    if len(radii) == low_radii:
        score += 100
    return score