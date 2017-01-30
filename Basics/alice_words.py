"""""""""""""""""""""""""""""
"  Created On: 19-Sep-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

fr = open("alice.txt", 'r', encoding='UTF-8')
fw = open("alice_words.txt", 'w', encoding='UTF-8')

dicto = {}
for word in fr.read().split():
    word = word.replace('_', ' ').replace('"', ' ').replace(',', ' ').replace('.', ' ')
    word = word.replace('-', ' ').replace('?', ' ').replace('!', ' ').replace("'", " ")
    word = word.replace('(', ' ').replace(')', ' ').replace(':', ' ').replace('[', ' ')
    word = word.replace(']', ' ').replace(';', ' ')

    # ignore case
    word = word.lower()

    if word.isalpha():
        if word not in dicto:
            dicto[word] = 1
        else:
            count = dicto.get(word)
            count += 1
            dicto[word] = count
words_list = list(dicto.keys())
words_list.sort()

for word in words_list:
    string = word + " = " + str(dicto[word])
    fw.write(string)
    fw.write("\n")

fr.close()
fw.close()

max_len = 0
for word in words_list:
    if len(word) > max_len:
        max_len = len(word)
        marker = word
print("The maximum length word is", marker)
print("Its length is ", str(max_len))
print("Its count is ", str(dicto[marker]))
