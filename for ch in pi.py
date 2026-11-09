#idea 2. buckshot roulet
import random
import math
#import tkinter use this for graphics 

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
    if blank_or_live0 + blank_or_live1 == 2:
        print("2 lives 0 blanks ToT")
    elif blank_or_live0 + blank_or_live1 == 1:
            print("1 lives 1 blanks")
    elif blank_or_live0 == 0 and blank_or_live1 == 0:
            print("0 lives 2 blanks :D")
elif int(shells) == 3:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2)]
    if blank_or_live0 + blank_or_live1 + blank_or_live2 == 3:
        print("3 lives 0 blanks O_O")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 == 2:
        print("2 lives 1 blanks")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 == 1:
        print("3 lives 2 blanks")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 == 0:
        print("0 lives 3 blanks :D")
elif int(shells) == 4:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3)]
    if blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 == 4:
        print("4 lives 0 blanks! good luck >:]")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 == 3:
        print("3 lives 1 blanks")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 == 2:
        print("2 lives 2 blanks")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 == 1:
        print("1 lives 3 blanks")
    elif blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 == 0:
        print("0 lives 4 blanks... boring...")
elif int(shells) == 5:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3), int(blank_or_live4)]
    if blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 5:
        print("5 lives and 0 BLANKS 🤣")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 4:
        print("4 lives 1 blanks")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 3:
        print("3 lives 2 blanks")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 2:
        print("2 lives 3 blanks")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 1:
        print("4 lives 1 blanks")
    elif  blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 == 0:
        print("")
elif int(shells) == 6:
    shotgun = [int(blank_or_live0), int(blank_or_live1), int(blank_or_live2), int(blank_or_live3), int(blank_or_live4), int(blank_or_live5)]

    if blank_or_live0 + blank_or_live1 + blank_or_live2 + blank_or_live3 + blank_or_live4 + blank_or_live5 == 6:
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
    print(shotgun)
else:
    print("what could you have possably done to get this text?...")
