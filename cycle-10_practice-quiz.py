# Author: IBN (AMDG) 1/27/2022
def food_costs(groceries,costs): 
    groceries_mod = groceries # set groceries_mod equal to work inside lists
    x = 0
    for lst in groceries: # each list in groceries
        for i, v in enumerate(lst): # enumerate
            lst[i] = "{0}: ${1}".format(v, costs[x])
            i += 1
            x += 1
    return groceries_mod

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt',]],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == ['apple: $1.99','pear: $2.99','banana: $0.99',],['salmon: $9.99','tuna: $10.99','cod:$6.99',],['milk: $3.49','eggs: $2.49','yogurt: $1.49'])