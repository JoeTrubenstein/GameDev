import random
import time

player_name = input("enter your name:  ")
player_stats = {"name": player_name, "health": 100}
victory_count = 0

print ("hello " + player_name)
time.sleep(1)
print ("you have " + str(player_stats["health"]) + " health")
time.sleep(1)
print ("defeat 3 enemies to best the dungeon")

while True:
    time.sleep(1)
    player_step = input("walk left, right, or straight? (enter l, r, or s...)")

    if player_step == "l" or player_step == "r" or player_step == "s":
        print ("you continue down the corridor")
        time.sleep(1)
        hit_or_miss = random.randint(1,2)
    else:
        print ("invalid input")
        time.sleep(1)
        continue

    while True:
        the_way = random.randint(1,3)
        
        if the_way == 1:
            print("You encounter a skeleton!")
            time.sleep(1)
            print("rolling for damage")
            enemy_damage = random.randint(0,50)
        elif the_way == 2:
            print("You encounter an orc!")
            time.sleep(1)
            print("rolling for damage")
            enemy_damage = random.randint(0,50)
        elif the_way == 3:
            print("You encounter a Dragon!")
            time.sleep(1)
            print("rolling for damage")
            enemy_damage = random.randint(0,100)

        if hit_or_miss == 1:
            time.sleep(1)
            print ("enemy hits for " + str(enemy_damage))
            player_stats["health"] = player_stats["health"] - enemy_damage
            time.sleep(1)
        else:
            time.sleep(1)
            print ("enemy defeated")
            time.sleep(1)
            victory_count = victory_count +1
            print ("victory count: " + str(victory_count))
    
        time.sleep(1)
        print ("player health is " + str(player_stats["health"]))
        break
        
    if player_stats["health"] < 0:
        time.sleep(1)
        print("you died...")
        break
    else:
        time.sleep(1)
        print ("you escape with your life")

    if victory_count == 3:
        time.sleep(1)
        print("you have bested the dungeon!")
        break
