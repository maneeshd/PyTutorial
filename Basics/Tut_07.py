"""""""""""""""""""""""""""""
"  Created On: 12-Aug-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

fw = open('sample.txt', 'w', encoding='UTF-8')
fw.write("Hello\tWorld\n")
fw.write('Scram')
fw.close()

fr = open('sample.txt', 'r', encoding='UTF-8')
print(fr.read())
fr.close()
