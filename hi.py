################################################################################################
#name this : Buckshot roulet... but in python!(unfinished)
#by -Boxy_boo on scratch (or youtube whenever i make a channle)
################################################################################################

#idea 2. buckshot roulet
import random
import math


hp = 5

#add randomizer for shells
shells = random.randint(2,8) 

#1 = live 0 = blank

#trying to put add value to shells if there live or blank

for shells in range(2, 8):
    blank_or_live0 = random.randint(0,1)
    blank_or_live1 = random.randint(0,1)
    blank_or_live2 = random.randint(0,1)
    blank_or_live3 = random.randint(0,1)
    blank_or_live4 = random.randint(0,1)
    blank_or_live5 = random.randint(0,1)
    blank_or_live6 = random.randint(0,1)
    blank_or_live7 = random.randint(0,1)

#finding the shell amount
if int(shells) == 2:
    shotgun = [int(blank_or_live0), int(blank_or_live1)]
    if int(blank_or_live0) + int(blank_or_live1) == 2:
        print("2 lives 0 blanks ToT")
    elif blank_or_live0 + blank_or_live1 == 1:
            print("1 lives 1 blanks")
    elif blank_or_live0 == 0 and blank_or_live1 == 0:
            print("0 lives 2 blanks :D")
elif int(shells) == 3:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2)]
    if int(blank_or_live0) + blank_or_live1 + blank_or_live2 == 3:
        print("3 lives 0 blanks O_O")
    elif int(blank_or_live0) + blank_or_live1 + blank_or_live2 == 2:
        print("2 lives 1 blanks")
    elif int(blank_or_live0) + blank_or_live1 + blank_or_live2 == 1:
        print("3 lives 2 blanks")
    elif int(blank_or_live0) + blank_or_live1 + blank_or_live2 == 0:
        print("0 lives 3 blanks :D")
elif int(shells) == 4:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3)]
    if int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 == 4:
        print("4 lives 0 blanks! good luck >:]")
    elif int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 == 3:
        print("3 lives 1 blanks")
    elif int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 == 2:
        print("2 lives 2 blanks")
    elif int(blank_or_live0) + blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 == 1:
        print("1 lives 3 blanks")
    elif int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 == 0:
        print("0 lives 4 blanks... boring...")
elif int(shells) == 5:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3), int(blank_or_live4)]
    if int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 5:
        print("5 lives and 0 BLANKS 🤣")
    elif  int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 4:
        print("4 lives 1 blanks")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 3:
        print("3 lives 2 blanks")
    elif  int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 2:
        print("2 lives 3 blanks")
    elif  int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 1:
        print("4 lives 1 blanks")
    elif  int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 0:
        print("0 lives and 5 blanks...")
elif int(shells) == 6:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3), int(blank_or_live4), int(blank_or_live5)]

    if int(blank_or_live0) + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 6:
        print("6 lives 0 blanks! oh boy!")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 5:
        print("")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 4:
        print("")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 3:
        print("")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 2:
        print("")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 1:
        print("")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 0:
        print("")
elif int(shells) == 7:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3), int(blank_or_live4), int(blank_or_live5), int(blank_or_live6)]
    if  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 + blank_or_live6 == 0:
        print("")
elif int(shells) == 8:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3), int(blank_or_live4), int(blank_or_live5), int(blank_or_live6), int(blank_or_live7)]
    if int(blank_or_live0) + int(blank_or_live1) + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 + blank_or_live6 + blank_or_live7 == 8:
        print("8 LIVES and 0 blank!... i think tucker looks funny...!")
else:
    print("what could you have possably done to get this text?...")


deathtext = random.randint(1, 10)
#check if the shell is live or blank after testing at us
if shells == 1:
    hp - 1
    if hp > 0:
        print("not so lucky, hu?")        
    elif hp == 0:
        print("too bad") or print("not so lucky hu?") or print("too bad")
    
else:
    print("lucky")





################################################################################################
#if you can make this a seprat folder if its on github
################################################################################################

#from operator import add

##2 game idea's
##1. make a game where the player has to guess to be greedy or not greedy.
##2. buckshot roulet, yes... buckshot roulet
##I atlest want to make a game of chanse

#coin = 6
#key = 4

#score = coin + key / 2

#addask = 0
#print(score)

#def player_input():
 
#    addask = input("number:")
#    return addask

#print("want more keys?")

#player_input()

#addkey = int(addask)

#fixkey = int(score) - int(coin) 
#dont forget float(Variable) int(Variable) Variable
#key = int(fixkey) * 2 + int(addkey)

 #int(key) == 100 or int(key) > 100 then == True: run(key = key / 0.5) save for later
#score = int(coin) + int(key) / 0.5 

#print(score)
################################################################################################