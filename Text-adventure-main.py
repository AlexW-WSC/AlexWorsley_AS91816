import world_map
import random


player_pos = 16, 2
player_max_health = 100
player_health = 60
player_gold = 10

player_alive = True

def StartSequence():
    global player_name
    player_name = input("What is your name?\n\n").title()
    ExplorationScreen(*player_pos)

def EndingSequence(Ending):
    print(Ending)



# inventory indexes 

weapon_inventory = {
    "Training Sword": 1,
    "Greatsword": 0,
    "Master Sword": 0,
}

healing_inventory = {
    "Potion": 1,
    "Elixir": 2,
    "silly potion": 0
}
armour_inventory = {
    "Chainmail": 1,
    "Leather Armour": 24,
    "test armour": 0
}
key_items_inventory = {
    "Ornate Key": 1,
}

# description indexes  

weapon_description_index = {
    "Training Sword": "A basic training sword. There were hundreds of these things lying around your hometown.",
    "Greatsword": "An impressive, heavy blade with significant power.", 
    "Master Sword": "The ultimate blade, forged from a dying star.",
}

healing_description_index = {
    "Potion": "The humble potion. Doesn't help much, but better than nothing."
}

armour_description_index = {
    "Chainmail": "idk 0w0 this is a placeholder, i'm tired"
}

key_item_description_index = {
    "Ornate Key": "An ornate, old key. looks like it would fit in a specific keyhole."
}


# value indexes

weapon_damage_index = {
    "Training Sword": 5,
    "Greatsword": 10,
    "Master Sword": 20,
}

healing_amount_index = {
    "Potion": 5,
    "Elixir": 10,
    "Shimmering Potion": 20,
    "Mega Pot": 50,
}

armour_reduction_index = {
    "Chainmail": 5
}


# Price index
weapon_price_index = {
    "Training Sword", 10
}

healing_price_index = {
    "Potion": 5,
    "Elixir": 15,
    "Shimmering Potion": 40,
    "Mega Pot": 100,
}

armour_price_index = {
    "Chainmail": 15
}

equipped_weapon = "Training Sword"
equipped_armour = "Chainmail"

# Battle System dictionaries 

healthbar_ui = ["[          ]","[-         ]","[--        ]","[---       ]","[----      ]","[-----     ]","[------    ]","[-------   ]","[--------  ]","[--------- ]", "[----------]"]


monster_index = {
    "Kingdom Outskirts": {
        "Bandit": {
            "Max Damage": 5,
            "Min Damage": 1,
            "Max Health": 20,
            "Min Health": 10,
            "Accuracy": 95,
        },

        "Wolf": {
            "Max Damage": 11,
            "Min Damage": 4,
            "Max Health": 16,
            "Min Health": 5,
            "Accuracy": 70,
        }
    },
}


#functions that actually do stuff!!! :0

def EquipWeapon(weapon):
    global equipped_weapon
    print(f"\nYou have equipped {weapon}. Your previous weapon was the {equipped_weapon}.\n\n———————————————————————————————————————————\n")
    weapon_inventory[equipped_weapon] += 1
    weapon_inventory[weapon] -= 1
    equipped_weapon = weapon

def EquipArmour(armour):
    global equipped_armour
    print(f"\nYou have equipped {armour}. Your previous armour was {equipped_armour}.\n\n———————————————————————————————————————————\n")
    armour_inventory[equipped_armour] += 1
    armour_inventory[armour] -= 1
    equipped_armour = armour

def UseHealing(healing_item):
    global player_max_health
    global player_health
    if player_health == player_max_health:
        print(f"\nThe {healing_item} will not have any effect! The {healing_item} was not consumed.")
        HealingMenu()
    elif player_health + healing_amount_index.get(healing_item) > player_max_health:
        temp = player_health + healing_amount_index.get(healing_item)
        difference = player_max_health - temp
        player_health = player_max_health
        print(f"\nThe {healing_item} healed you to full health. Your health is now {player_health}. (Healed {(healing_amount_index.get(healing_item) + difference)} health)\n\n———————————————————————————————————————————\n")
        healing_inventory[healing_item] -= 1
        HealingMenu()
    else:
        player_health += healing_amount_index.get(healing_item)
        print(f"\nYou used the {healing_item}. Your health is now {player_health}. (Healed {healing_amount_index.get(healing_item)} health)\n\n———————————————————————————————————————————\n")
        healing_inventory[healing_item] -= 1
    

# nested menus 


def CheckWeapon(weapon):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{weapon}: {weapon_damage_index.get(weapon)} ATK\n\n“{weapon_description_index.get(weapon)}”\n")
            print("   1. Equip Weapon\n   2. Back to Weapons Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1:
                player_action_taken = True
                EquipWeapon(weapon)
                WeaponsMenu()
            elif decision == 2:
                player_action_taken = True
                WeaponsMenu()
            else:
                print("Please enter a valid number!\n")
                



def CheckHealing(healing_item):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{healing_item}: {healing_amount_index.get(healing_item)} HEAL\n\n“{healing_description_index.get(healing_item)}”\n")
            print("   1. Use Healing Item\n   2. Back to Healing Items Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1:
                player_action_taken = True
                UseHealing(healing_item)
                HealingMenu()
            elif decision == 2:
                player_action_taken = True
                HealingMenu()
            else:
                print("Please enter a valid number!\n")
            
            
def CheckArmour(armour):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{armour}: {armour_reduction_index.get(armour)} DEF\n\n“{armour_description_index.get(armour)}”\n")
            print("   1. Equip Armour\n   2. Back to Armour Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else: 
            if decision == 1:
                player_action_taken = True
                EquipArmour(armour)
                ArmourMenu()
            elif decision == 2:
                player_action_taken = True
                ArmourMenu()
            else:
                print("Please enter a valid number!\n")
            


def CheckKeyItem(key_item):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{key_item}\n\n“{armour_description_index.get(key_item)}”\n")
            print("   1. Back to Key Item Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else: 
            if decision == 1:
                player_action_taken = True
                KeyItemsMenu()
            else:
                print("Please enter a valid number!\n")




# core menus 

def ShopMenu(x,y):
    global player_gold
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"{world_map.tile_map.get((x,y)).get("Name")}: Shop Menu - {player_gold} Gold\n")
            i = 1
            for item in world_map.tile_map.get((x,y)).get("Shop Contents"):
                if item in weapon_price_index:
                    print(f"   {i}. {item}: {weapon_price_index.get(item)} Gold")
                    i += 1
                elif item in healing_price_index:
                    print(f"   {i}. {item}: {healing_price_index.get(item)} Gold")
                    i += 1
                elif item in armour_price_index:
                    print(f"   {i}. {item}: {armour_price_index.get(item)} Gold")
                    i += 1
            print(f"\n   {i}. Back to Exploration Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == i:
                player_action_taken = True
                ExplorationScreen(x,y)
            elif decision > len(world_map.tile_map.get((x,y)).get("Shop Contents")):
                    print("Please enter a valid number!\n")
            else:
                 for item in world_map.tile_map.get((x,y)).get("Shop Contents"):
                    if decision == (world_map.tile_map.get((x,y)).get("Shop Contents").index(item) + 1):
                        if item in weapon_price_index:
                            if player_gold - weapon_price_index.get(item) < 0:
                                player_action_taken = True
                                print(f"You do not have enough money! This item costs {weapon_price_index.get(item)} Gold but you only have {player_gold} Gold!\n")
                                ShopMenu(x,y)
                            else:
                                player_action_taken = True
                                player_gold -= weapon_price_index.get(item)
                                print(f"You have purchased the {item}, which cost {weapon_price_index.get(item)} Gold. Your new balance is {player_gold} Gold.\n")
                                ShopMenu(x,y)
                        elif item in healing_price_index:
                            if player_gold - healing_price_index.get(item) < 0:
                                player_action_taken = True
                                print(f"You do not have enough money! This item costs {healing_price_index.get(item)} Gold but you only have {player_gold} Gold!\n")
                                ShopMenu(x,y)
                            else:
                                player_action_taken = True
                                player_gold -= healing_price_index.get(item)
                                print(f"You have purchased the {item}, which cost {healing_price_index.get(item)} Gold. Your new balance is {player_gold} Gold.\n")
                                ShopMenu(x,y)
                        elif item in armour_price_index:
                            if player_gold - armour_price_index(item) < 0:
                                player_action_taken = True
                                print(f"You do not have enough money! This item costs {armour_price_index.get(item)} Gold but you only have {player_gold} Gold!\n")
                                ShopMenu(x,y)
                            else:
                                player_action_taken = True
                                player_gold -= armour_price_index.get(item)
                                print(f"You have purchased the {item}, which cost {armour_price_index.get(item)} Gold. Your new balance is {player_gold} Gold.\n")
                                ShopMenu(x,y)

                        
                        
            

    
    

def WeaponsMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
            try:
                print(f"\n1. Weapons Menu: {equipped_weapon} currently equipped\n")
                weapon_list = list(weapon_inventory)
                weapon_amount_list = list(weapon_inventory.values())
                i = 1
                for weapon in weapon_list:
                        if weapon_amount_list[weapon_list.index(weapon)] > 1:
                            print(f"   {i}. {weapon} (x{weapon_amount_list[weapon_list.index(weapon)]})")
                            i += 1
                        elif weapon_amount_list[weapon_list.index(weapon)] == 1:
                            print(f"   {i}. {weapon}")
                            i += 1
                print(f"\n   {i}.  Back to Bag Menu\n\n———————————————————————————————————————————\n")
                decision = int(input())
            except ValueError: 
                print("Please enter a valid number!\n")
            else:
                if decision == i:
                    player_action_taken = True
                    BagMenu()
                elif decision > len(weapon_list):
                    print("Please enter a valid number!\n")
                elif weapon_amount_list[decision - 1] == 0:
                    print("Please enter a valid number!\n")
                else:
                    for weapon in weapon_list:
                        if decision == (weapon_list.index(weapon) + 1):
                            player_action_taken = True
                            CheckWeapon(weapon)
                            
                
def HealingMenu():
    decision = 0 
    player_action_taken = False
    while player_action_taken == False:
        try:
            print("\n2. Healing Menu\n")
            healing_list = list(healing_inventory)
            healing_amount_list = list(healing_inventory.values())
            i = 1 
            for healing_item in healing_list:
                if healing_amount_list[healing_list.index(healing_item)] > 1:
                    print(f"   {i}. {healing_item} (x{healing_amount_list[healing_list.index(healing_item)]})")
                    i += 1
                elif healing_amount_list[healing_list.index(healing_item)] == 1:
                    print(f"   {i}. {healing_item}")
                    i += 1
            print(f"\n   {i}. Back to Bag Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == i:
                player_action_taken = True
                BagMenu()
            elif decision > len(healing_list):
                print("Please enter a valid number!\n")
            elif healing_amount_list[decision - 1] == 0:
                print("Please enter a valid number!\n")
            else:
                for healing_item in healing_list:
                    if decision == (healing_list.index(healing_item)+ 1):
                        player_action_taken = True 
                        CheckHealing(healing_item)



        

def ArmourMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print("\n3. Armour Menu\n")
            armour_list = list(armour_inventory)
            armour_amount_list = list(armour_inventory.values())
            i = 1
            for armour in armour_list:
                if armour_amount_list[armour_list.index(armour)] > 1:
                    print(f"   {i}. {armour} (x{armour_amount_list[armour_list.index(armour)]})")
                    i += 1
                elif armour_amount_list[armour_list.index(armour)] == 1:
                    print(f"   {i}. {armour}")
                    i += 1
            print(f"\n   {i}. Back to Bag Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == i:
                player_action_taken = True
                BagMenu()
            elif decision > len(armour_list):
                print("Please enter a valid number!\n")
            elif armour_amount_list[decision - 1] == 0:
                print("Please enter a valid number!\n")
            else:
                for armour in armour_list:
                    if decision == (armour_list.index(armour)+ 1):
                        player_action_taken = True 
                        CheckArmour(armour)

def KeyItemsMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print("\n4. Key Items Menu\n")
            key_items_list = list(key_items_inventory)
            key_items_amount_list = list(key_items_inventory.values())
            i = 1
            for key_item in key_items_list:
                print(f"   {i}. {key_item}")
                i += 1
            print(f"\n   {i}. Back to Bag Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == i:
                player_action_taken = True 
                BagMenu()
            elif decision > len(key_items_list):
                print("Please enter a valid number!\n")
            elif key_items_amount_list[decision - 1] == 0:
                print("Please enter a valid number!\n")
            else:
                for key_item in key_items_list:
                    if decision == (key_items_list.index(key_item)+ 1):
                        player_action_taken = True 
                        CheckKeyItem(key_item)

def BagMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:

        try:
            print("\n3. Bag Menu\n\nWhich pocket would you like to inspect?\n\n   1. Weaponry\n   2. Medicine\n   3. Armour\n   4. Key Items\n\n   5. Back to Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1:
                player_action_taken = True
                WeaponsMenu()
            elif decision == 2:
                player_action_taken = True
                HealingMenu()
            elif decision == 3:
                player_action_taken = True
                ArmourMenu()
            elif decision == 4:
                player_action_taken = True
                KeyItemsMenu()
            elif decision == 5:
                player_action_taken = True
                ExplorationScreen(*player_pos)
            else:
                print("Please enter a valid number!\n")
            




def MovementMenu(x,y):
    global player_pos
    decision = 0
    player_action_taken = False
    while player_action_taken == False: 
        try:
            east_tile = None
            west_tile = None
            north_tile = None 
            south_tile = None
            print(f"\n2. Movement Menu - (X:{x},Y:{y})\n")
            try:
                print(f"   1. Move East (Positive X), [X:{x+1}, Y:{y}] - {world_map.tile_map.get((x+1,y)).get("Type")} Tile: “{world_map.tile_map.get((x+1,y)).get("Name")}”") 
            except AttributeError:
                print(f"   1. Move East (Positive X), [X:{x+1}, Y:{y}] - “Obstructed”")
                east_tile = "invalid"
            try:
                print(f"   2. Move West (Negative X), [X:{x-1}], Y:{y}] - {world_map.tile_map.get((x-1,y)).get("Type")} Tile: “{world_map.tile_map.get((x-1,y)).get("Name")}”") 
            except AttributeError:
                print(f"   2. Move West (Negative X), [X:{x-1}], Y:{y}] - “Obstructed”")
                west_tile = "invalid"
            try: 
                print(f"   3. Move North (Positive Y) [X:{x}, Y:{y+1}] - {world_map.tile_map.get((x,y+1)).get("Type")} Tile: “{world_map.tile_map.get((x,y+1)).get("Name")}”") 
            except AttributeError:
                print(f"   3. Move North (Positive Y) [X:{x}, Y:{y+1}] - “Obstructed”")
                north_tile = "invalid"
            try: 
                print(f"   4. Move South (Negative Y) [X:{x}, Y:{y-1}] - “{world_map.tile_map.get((x,y-1)).get("Name")}”\n")
            except AttributeError:
                print(f"   4. Move South (Negative Y) [X:{x}, Y:{y-1}] - “Obstructed”\n")
            print("   5. Back to Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
            
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1 and east_tile != "invalid":
                player_action_taken = True 
                print(f"\nYou have moved East. [X:{x+1}, Y:{y}] - {world_map.tile_map.get((x+1,y)).get("Type")} Tile: “{world_map.tile_map.get((x+1,y)).get("Name")}”")
                player_pos = (x+1, y)
                ExplorationScreen(*player_pos)
            elif decision == 1 and east_tile == "invalid":
                print("\nThis tile is obstructed!")
            elif decision == 2 and west_tile != "invalid":
                player_action_taken = True
                print(f"\nYou have moved West. [X:{x-1}, Y:{y}] - {world_map.tile_map.get((x-1,y)).get("Type")} Tile: “{world_map.tile_map.get((x-1,y)).get("Name")}”")
                player_pos = (x-1, y)
                ExplorationScreen(*player_pos)
            elif decision == 2 and west_tile == "invalid":
                print("\nThis tile is obstructed!")
            elif decision == 3 and north_tile != "invalid":
                player_action_taken = True
                print(f"\nYou have moved North. [X:{x}, Y:{y+1}] - {world_map.tile_map.get((x,y+1)).get("Type")} Tile: “{world_map.tile_map.get((x,y+1)).get("Name")}”")
                player_pos = (x, y+1)
                ExplorationScreen(*player_pos)
            elif decision == 3 and north_tile == "invalid":
                print("\nThis tile is obstructed!")
            elif decision == 4 and south_tile != "invalid":
                player_action_taken = True
                print(f"\nYou have moved South. [X:{x}, Y:{y-1}] - {world_map.tile_map.get((x,y-1)).get("Type")} Tile: “{world_map.tile_map.get((x,y-1)).get("Name")}")
                player_pos = (x, y-1)
                ExplorationScreen(*player_pos)
            elif decision == 4 and south_tile == "invalid":
                print("\nThis tile is obstructed!")
            elif decision == 5:
                player_action_taken = True
                ExplorationScreen(*player_pos)
            else:
                print("Please enter a valid number!\n")


def Interaction(x,y):
    world_map.tile_map.get((x,y)).update({"Interacted": True})
    print(f"\n“{world_map.tile_map.get((x,y)).get("Interaction Text")}.”\n")
    if world_map.tile_map.get((x,y)).get("Reward Amount") == 1:
        print(f"You found the {world_map.tile_map.get((x,y)).get("Reward")}.")
        if world_map.tile_map.get((x,y)).get("Reward") in weapon_inventory:
            weapon_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
        elif world_map.tile_map.get((x,y)).get("Reward") in healing_inventory:
            healing_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
        elif world_map.tile_map.get((x,y)).get("Reward") in  armour_inventory:
            armour_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
            ExplorationScreen(x,y)
        elif world_map.tile_map.get((x,y)).get("Reward") in key_items_inventory:
            key_items_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
        ExplorationScreen(x,y)
    else:
        print(f"You found the {world_map.tile_map.get((x,y)).get("Reward")} (x{world_map.tile_map.get((x,y)).get("Reward Amount")}).")
        if world_map.tile_map.get((x,y)).get("Reward") in weapon_inventory:
            weapon_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
        elif world_map.tile_map.get((x,y)).get("Reward") in healing_inventory:
            healing_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
        elif world_map.tile_map.get((x,y)).get("Reward") in  armour_inventory:
            armour_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
        elif world_map.tile_map.get((x,y)).get("Reward") in key_items_inventory:
            key_items_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
        ExplorationScreen(x,y)


def UseBattleHealing(healing_item):
    global player_max_health
    global player_health
    if player_health == player_max_health:
        print(f"\nThe {healing_item} will not have any effect! The {healing_item} was not consumed.")
        return False
    elif player_health + healing_amount_index.get(healing_item) > player_max_health:
        temp = player_health + healing_amount_index.get(healing_item)
        difference = player_max_health - temp
        player_health = player_max_health
        print(f"\nThe {healing_item} healed you to full health. Your health is now {player_health}. (Healed {(healing_amount_index.get(healing_item) + difference)} health)\n\n———————————————————————————————————————————\n")
        healing_inventory[healing_item] -= 1
        return True # value for checking if turn has actually been used, passed thrrough the functions
    else:
        player_health += healing_amount_index.get(healing_item)
        print(f"\nYou used the {healing_item}. Your health is now {player_health}. (Healed {healing_amount_index.get(healing_item)} health)\n\n———————————————————————————————————————————\n")
        healing_inventory[healing_item] -= 1
        return True


def CheckBattleHealing(healing_item):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{healing_item}: {healing_amount_index.get(healing_item)} HEAL\n\n“{healing_description_index.get(healing_item)}”\n")
            print("   1. Use Healing Item\n   2. Back to Battle Healing Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1:
                player_action_taken = True
                return UseBattleHealing(healing_item) # Boolean

            elif decision == 2:
                player_action_taken = True
                return False
            else:
                print("Please enter a valid number!\n")

def BattleHealingMenu():
    decision = 0 
    player_action_taken = False
    while player_action_taken == False:
        try:
            print("\n2. Battle Healing Menu\n")
            healing_list = list(healing_inventory)
            healing_amount_list = list(healing_inventory.values())
            i = 1 
            for healing_item in healing_list:
                if healing_amount_list[healing_list.index(healing_item)] > 1:
                    print(f"   {i}. {healing_item} (x{healing_amount_list[healing_list.index(healing_item)]})")
                    i += 1
                elif healing_amount_list[healing_list.index(healing_item)] == 1:
                    print(f"   {i}. {healing_item}")
                    i += 1
            print(f"\n   {i}. Back to Battle Encounter\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == i:
                player_action_taken = True
                return False
            elif decision > len(healing_list):
                print("Please enter a valid number!\n")
            elif healing_amount_list[decision - 1] == 0:
                print("Please enter a valid number!\n")
            else:
                for healing_item in healing_list:
                    if decision == (healing_list.index(healing_item)+ 1):
                        player_action_taken = True 
                        return CheckBattleHealing(healing_item)


#Encounter System used on Battle tiles - could certainly be more efficient.
def EnemyEncounter(x,y):
    global player_max_health
    global player_health

    player_damage = weapon_damage_index[equipped_weapon]
    player_damage_reduction = armour_reduction_index[equipped_armour]
    
    if world_map.tile_map.get((x,y)).get("Location") == "Kingdom Outskirts":
        monster_list = list(monster_index.get(world_map.tile_map.get((x,y)).get("Location")))
        monster = random.choice(monster_list)
        monster_max_hp = random.randint(monster_index.get("Kingdom Outskirts").get(monster).get("Min Health"), monster_index.get("Kingdom Outskirts").get(monster).get("Max Health"))
        monster_accuracy = monster_index.get("Kingdom Outskirts").get(monster).get("Accuracy")
        monster_min_damage = monster_index.get("Kingdom Outskirts").get(monster).get("Min Damage")
        monster_max_damage = monster_index.get("Kingdom Outskirts").get(monster).get("Max Damage")

    # elif cave, cliffs, forest, etc.
    
    monster_hp = monster_max_hp
    turn = 1
    print("\n1. Enemy Encounter")


    while monster_hp > 0 and player_health > 0:
        print(f"\nTurn {turn} \n")

        # UI things 
        monster_health_percent = 100 * float(monster_hp) / float(monster_max_hp)
        monster_ui_bar_index = min(int(monster_health_percent // 10), 10)

        player_health_percent = 100 * float(player_health) / float(player_max_health)
        player_ui_bar_index = min(int(player_health_percent // 10), 10)

        decision = 0
        player_action_taken = False
        while player_action_taken == False:
            try:
                print(f"\n{monster}: {healthbar_ui[monster_ui_bar_index]} {round(monster_hp, 2)}/{round(monster_max_hp, 2)} HP\n\n{player_name}: {healthbar_ui[player_ui_bar_index]} {round(player_health, 2)}/{round(player_max_health, 2)} HP\n")
                print("Battle Options:\n")
                print(f"   1. Attack ({equipped_weapon})\n   2. Healing\n\n———————————————————————————————————————————\n")
                decision = int(input())
            except ValueError:
                print("Please enter a valid number!\n")
            else:
                if decision == 1: # Attack 
                    player_action_taken = True
                    print(f"\nYou attack the {monster} with your {equipped_weapon}! The {monster} takes {player_damage} damage.")
                    # damage time 
                    monster_hp -= player_damage
                    
                elif decision == 2:
                    player_action_taken = BattleHealingMenu()
                else:
                    print("Please enter a valid number!\n")


        # Enemy Turn 
        if monster_hp > 0:
            hit_roll = random.randint(1, 100)
            if hit_roll <= monster_accuracy:
                true_damage = random.randint(monster_min_damage, monster_max_damage)
                damage_taken = max(0, true_damage - player_damage_reduction)
                print(f"The {monster} attacks you. You take {damage_taken} damage.")
                player_health -= damage_taken
            else: 
                print(f"The {monster} attacks but misses!")
            
        turn += 1
    
    # Post-Battle calculations 

    if player_health <= 0:
        EndingSequence("Bad Ending")
    elif monster_hp <= 0:
        ## finsih this later 
        print("\nBattle-Win")
        world_map.tile_map.get((x,y)).update({"Battle Complete": True})
        ExplorationScreen(x,y)


def ExplorationScreen(x,y):
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            if world_map.tile_map.get((x,y)).get("Type") == "Plain":
                print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. No Option Availiable\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            elif world_map.tile_map.get((x,y)).get("Type") == "Battle":
                if world_map.tile_map.get((x,y)).get("Battle Complete") == True:
                    print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {world_map.tile_map.get((x,y)).get("Type")} (Completed)\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
                else:
                    print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {world_map.tile_map.get((x,y)).get("Type")}\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            else:
                print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {world_map.tile_map.get((x,y)).get("Type")}\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("\nPlease enter a valid number!\n")
        else:
            if decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Interact":
                player_action_taken = True
                Interaction(x,y)
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Battle":
                if world_map.tile_map.get((x,y)).get("Battle Complete") == True:
                    print("\nYou have already completed this battle!\n")
                if world_map.tile_map.get((x,y)).get("Battle Complete") == False:
                    player_action_taken = True
                    EnemyEncounter(x,y)
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Shop":
                player_action_taken = True
                ShopMenu(x,y)
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Plain":
                print("\nPlease enter a valid number!\n")
            elif decision == 2:
                player_action_taken = True
                MovementMenu(x,y)
                
            elif decision == 3:
                player_action_taken = True
                BagMenu()
                
            else:
                print("\nPlease enter a valid number!\n")




# it all runs from calling one beautiful function :3
StartSequence()

