"""""""""""""""""""""""""""""
"  Created On: 19-Sep-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

trans = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'boy': 'matey', 'madam': 'proud beauty',
         'professor': 'foul blaggart',
         'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr', 'students': 'swabbies', 'are': 'be',
         'lawyer': 'foul blaggart', 'the': 'th’',
         'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be', 'man': 'matey'}

english = str(input("Enter the sentence in english: "))

pirate = ""
for word in english.split():
    if word in trans:
        pirate = pirate + str(trans[word]) + " "
    else:
        pirate = pirate + str(word) + " "
print("Pirate translated shit=", pirate)
