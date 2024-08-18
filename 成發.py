import random
import time
class GAY_DETECTED(Exception):
    def __init__(self):
        super().__init__("ENGLISH OR SPANISH?")
        
Chosen=int (input("Rock(1), Paper(2), Scissors(3)? : "))

NPC = (random.randint(1,3))
Sum = NPC + Chosen

if Sum%3 == 0:
    if Chosen == 1:
        print ("NPC chose ROCK too. Draw.")
    if Chosen == 2:
        print ("NPC chose PAPER too. Draw.")
    if Chosen == 3:
        print ("NPC chose SCISSORS too. Draw.")
    time.sleep(1)
    print("Seems like, we need to have a 學測 BATTLE.")
    time.sleep(1)
    print("Answer the next 4 questions!")
    time.sleep(1)
    for (i) in range(4):
        NPC = (random.randint(1,10))
        if NPC == 1:
            Answer = float(input("pi 到小數點後十位=? : "))
            if Answer == 3.1415926535:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 2:
            Answer = float(input("絕對零度=?(攝氏) : "))
            if Answer == -273.15:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 3:
            Answer = int(input("光速=?(m/s, 精確值) : "))
            if Answer == 299792458:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 4:
            Answer = float(input("重力加速度=?(m/s^2, 精確值) : "))
            if Answer == 9.80665:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 5:
            Answer = float(input("電子電量=?(庫倫, 打前段(format : a.bcd)) : "))
            if Answer == -1.602:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 6:
            Answer = int(input("中子電量是電子的幾倍?(整數) : "))
            if Answer == 1836:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 7:
            Answer = int(input("黃金比例到小數點第十位? : "))
            if Answer == 1.6180339887:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 8:
            Answer = int(input("黑船事件發生年分? : "))
            if Answer == 1853:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 9:
            Answer = int(input("建中(的前生)創校於哪一年? : "))
            if Answer == 1898:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
        if NPC == 10:
            Answer = int(input("北一(的前生)創校於哪一年? : "))
            if Answer == 1904:
                    print("Correct.")
            else:
                    print("Welp.")
                    print("Remember, son? Losing is GAY")
                    time.sleep(1)
                    raise GAY_DETECTED
    print("Welp, I guess you win.")
if Sum%3 == 1:
    if Chosen == 1:
        print("NPC chose PAPER. You lost :skull:")
    if Chosen == 2:
        print("NPC chose SCISSORS. You lost :skull:")
    if Chosen == 3:
        print("NPC chose ROCK. You lost :skull:")
    time.sleep(1)
    print("SKILL_ISSUE_DETECTED")
    print("Remember, son? Losing is GAY")
    time.sleep(1)
    raise GAY_DETECTED
if Sum % 3 == 2:
    if Chosen == 1:
        print("NPC chose SCISSORS. Fine... you win. Another round?")
    if Chosen == 2:
        print("NPC chose ROCK. Fine... you win. Another round?")
    if Chosen == 3:
        print("NPC chose PAPER. Fine... you win. Another round?")