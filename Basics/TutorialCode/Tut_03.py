"""""""""""""""""""""""""""""
"  Created On: 20-Jul-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

ageLimit = 18

age = input('Enter the __age: ')

if age > ageLimit:
    print('Hello')
elif (age > 0) and (age < ageLimit):
    print('Nope')
else:
    print('U r not born yet')
