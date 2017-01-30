"""""""""""""""""""""""""""""
"  Created On: 14-Sep-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""


def remove_dups(astring):
    no_dups = ""
    alpha = list(astring)
    for char in alpha:
        if char not in no_dups:
            no_dups += str(char)
    return no_dups


print(remove_dups("Mississippi"))  # should print Misp
