from operator import add

#2 game idea's
#1. make a game where the player has to guess to be greedy or not greedy.
#2. buckshot roulet, yes... buckshot roulet
#I atlest want to make a game of chanse

coin = 6
key = 4

score = coin + key / 2

addask = 0
print(score)

def player_input():
 
    addask = input("number:")
    return addask

print("want more keys?")

player_input()

addkey = int(addask)

fixkey = int(score) - int(coin) 
#dont forget float(Variable) int(Variable) Variable
key = int(fixkey) * 2 + int(addkey)

 #int(key) == 100 or int(key) > 100 then == True: run(key = key / 0.5) save for later
score = int(coin) + int(key) / 0.5 

print(score)

