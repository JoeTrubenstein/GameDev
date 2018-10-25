import random
import time

pName = input("enter your name:  ")
stats = {"name": pName, "health": 100}
victories = 0

print ("hello " + pName)
time.sleep(1)
print ("you have " + str(stats["health"]) + " health")
time.sleep(1)
print ("defeat 3 enemies to best the dungeon")

while True:
    time.sleep(1)
    pStep = input("walk left, right, or straight? (enter l, r, or s...)")

    if pStep == "l" or pStep == "r" or pStep == "s":
        print ("you continue down the corridor")
        time.sleep(1)
        hitMiss = random.randint(1,2)
    else:
        print ("invalid input")
        time.sleep(1)
        continue

    while True:
        theWay = random.randint(1,3)
        
        if theWay == 1:
            print("You encounter a skeleton!")
            time.sleep(1)
            print("rolling for damage")
            eDmg = random.randint(0,50)
        elif theWay == 2:
            print("You encounter an orc!")
            time.sleep(1)
            print("rolling for damage")
            eDmg = random.randint(0,50)
        elif theWay == 3:
            print("You encounter a Dragon!")
            time.sleep(1)
            print("rolling for damage")
            eDmg = random.randint(0,100)

        if hitMiss == 1:
            time.sleep(1)
            print ("enemy hits for " + str(eDmg))
            stats["health"] = stats["health"] - eDmg
            time.sleep(1)
        else:
            time.sleep(1)
            print ("enemy defeated")
            time.sleep(1)
            victories = victories+1
            print ("victory count: " + str(victories))
    
        time.sleep(1)
        print ("player health is " + str(stats["health"]))
        break
        
    if stats["health"] < 0:
        time.sleep(1)
        print("you died...")
        break
    else:
        time.sleep(1)
        print ("you escape with your life")

    if victories == 3:
        time.sleep(1)
        print("you have bested the dungeon!")
        break
