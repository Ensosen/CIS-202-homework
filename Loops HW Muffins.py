# You work for a bakery that sells two items: muffins and cupcakes. The number of muffins and cupcakes in your shop at any given time is stored in the variables muffins and cupcakes which you will define, and the store has 10 muffins and 10 cupcakes.  Write a program that takes strings from standard input indicating what your customers are buying ("muffin" for a muffin, "cupcake" for a cupcake). If they buy a muffin, decrease muffins by one, and if they buy a cupcake, decrease cupcakes by 1. If there is no more of that baked good left, print ("Out of stock").  Once you are done selling, input "0", and have the program print out the number of muffins and cupcakes remaining, in the form "muffins: 9 cupcakes: 3" (if there were 9 muffins and 3 cupcakes left, for example).

# Constants

muffins = 10
cupcakes = 10
sale = ('')

# Promps for sales
while sale != '0':
    sale = input('Would you like a muffin or cupcake? ')
    if sale == 'muffin':
        if muffins == 0: print ('Out of Stock')
        if muffins > 0: muffins = muffins - 1
    elif sale == 'cupcake':
        if cupcakes == 0: print ('Out of Stock')
        if cupcakes > 0: cupcakes = cupcakes - 1
    elif sale == '0':break
    else: print ('Sorry, please type either "muffin" or "cupcake". If you are done for the day type 0 to end.')
# End message
print ('Muffins:',muffins,)
print ('Cupcakes:',cupcakes,)
    


