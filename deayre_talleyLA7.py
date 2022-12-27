inventory = {"apples": 1.0,
 "bacon": 3.0,
 "lettuce": 2.5,
 "milk": 3.75,
 "ale" : 7.5}

cart = {}
for i in inventory:
    print("How many amounts of  ", i, " will you be buying today?\n")
    q =int(input("type amount: "))
    cart[i]=[q,q*inventory[i]]
     #price = q * p
     #print(price)
print(cart)
total = 0

print("checkout recepit: ", '\t', 'item', '\t', 'price')

#this creates the checkout list at the end of the program 
for t in cart:
    print('\n', t, '\t', cart[t][0],'\t', cart[t][1])
    total = total + cart[t][1]
    
print("Cart total: ", total)