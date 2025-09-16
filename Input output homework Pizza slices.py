print ('Assume each pizza has 8 slices. Assume that there is a family of 4. Ask how many slices each person in the family eats. Then calculate how many whole pizzas you need to order and how many pizza slices are leftover after everyone is done eating.')
#   Gathering the inputs needed for problem.
slices1 = int(input('How many slices will the first person eat? '))
slices2 = int(input('How many slices will the second person eat? '))
slices3 = int(input('How many slices will the third person eat? '))
slices4 = int(input('How many slices will the fourth person eat? '))
#   Adding input into the amount of ordered slices and displaying the amount ordered.
orderdslc = slices1 + slices2 + slices3 + slices4
print ('All together that is',orderdslc,'slices total.')
#   Using True false statement to work out the possibility of getting a 0 on total pizza needed,
# while still keeping the correct number of pizza.
ttlza = orderdslc//8+(orderdslc%8>0)
#   Using math to then gain the slices total and subtracting the ordered amount.
ttlslc = ttlza*8
leftover = ttlslc-orderdslc

#   I then took the float amounts and turned them into integers to remove the .0 at the end.
# This step was optional but it just made the final print look prettier.
leftover = int(float(leftover))
ttlza = int(float(ttlza))
# I then made text that would display the final answers in a clear message that looks nice.
print ('You need to order',ttlza,'pizza(s). That will leave you with,',leftover,'pizza'
       ' slice(s) left over.')
