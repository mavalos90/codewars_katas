# How long each order will take
# 6 kyu

'''
The pizza store wants to know how long each order will take. They know:

Prepping a pizza takes 3 mins
Cook a pizza takes 10 mins
Every salad takes 3 mins to make
Every appetizer takes 5 mins to make
There are 2 pizza ovens
5 pizzas can fit in a oven
Prepping for a pizza must be done before it can be put in the oven
There are two pizza chefs and one chef for appitizers and salads combined
The two pizza chefs can work on the same pizza
Write a function, order, which will tell the company how much time the order will take.

See example tests for details.

'''

def order(pizzas, salads, appetizers):  
    pizza_time = 3 * (pizzas / 2) + 10 * ((pizzas // 11) + 1)
    other_time = 3 * salads + 5 * appetizers

    return max(other_time, pizza_time)