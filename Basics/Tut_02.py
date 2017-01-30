"""""""""""""""""""""""""""""
"  Created On: 20-Jul-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

players = ['Ronaldo', 'Messi', 'Xavi', 'Iniesta']
print(players)
players.append(7)
players.append(10)
players.append(6)
players.append(8)
print(players)
print(players[int((1 + 2) / 2)])
print(players[2:])
print(players[2:3])
print(players[3:])

players[:2] = [0, 0]

print(players)

players[:2] = []

print(players)

players = []
