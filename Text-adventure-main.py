player_pos = 16, 2
player_max_health = 100
player_health = 97

healthbar_ui = ["[          ]","[-         ]","[--        ]","[---       ]","[----      ]","[-----     ]","[------    ]","[-------   ]","[--------  ]","[--------- ]", "[----------]"]

player_alive = True

def StartSequence():
    return


# map index 
tile_map = {
    
    (16, 2): {
        "Location": "Kingdom Outskirts",
        "Name": "Grassland",
        "Description":"You see many cats.",
        "Type": "Interact",
        "Interacted": False,
        "Battle Complete": None,
        "Reward Obtained": None,
        "Reward": None,
        "Reward Amount": None,
    },
    
    (-1,1): {
        "Location": "Kingdom Outskirts",
        "Name": "Grassland",
        "Type": "Interact",
        "Interacted": False,
        "Battle Complete": None,
        "Reward Obtained": None,
    },



    (0,1): {
        "Location": "Kingdom Outskirts",
        "Name": "Grassland",
        "Type": "Interact",
        "Interacted": False,
        "Battle Complete": None,
        "Reward Obtained": None,
    },

    (1,1): {
        "Location": "Kingdom Outskirts",
        "Name": "Grassland",
        "Type": "Interact",
        "Interacted": False,
        "Battle Complete": None,
        "Reward Obtained": None,
    },

    (-1,0): {
        "Location": "Kingdom Outskirts",
        "Name": "Grassland",
        "Type": "Interact",
        "Interacted": False,
        "Battle Complete": None,
        "Reward Obtained": None,
    },
    
    (0,0): {
        "Location": "Kingdom Outskirts",
        "Name": "Grassland",
        "Type": "Interact",
        "Interacted": False,
        "Battle Complete": None,
        "Reward Obtained": None,
    },
    (1,0): {
        "Location": "Kingdom Outskirts",
        "Name": "Meow",
        "Description":"You see many cats.",
        "Type": "Battle",
        "Interacted": None,
        "Battle Complete": False,
        "Reward Obtained": None,
    }
}



# inventory indexes 

weapon_inventory = {
    "Training Sword": 1,
    "Greatsword": 3,
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
key_item_inventory = {
    "OrnateKey": 1,
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


# more indexes !!!

weapon_damage_index = {
    "Training Sword": 5,
}

healing_amount_index = {
    "Potion": 5,
    "Elixr": 10,
    "Shimmering Potion": 20,
    "Good healing item": 50,
}

equipped_weapon = "Master Sword"
equipped_armour = "test armour"

def EquipWeapon(weapon):
    global equipped_weapon
    print(f"\nYou have equipped {weapon}. Your previous weapon was the {equipped_weapon}.\n\n———————————————————————————————————————————\n")
    weapon_inventory[equipped_weapon] += 1
    weapon_inventory[weapon] -= 1
    equipped_weapon = weapon

def EquipArmour(armour):
    global equipped_armour
    print(f"\nYou have equipped {armour}. Your previous armour was the {equipped_armour}.\n\n———————————————————————————————————————————\n")
    armour_inventory[equipped_armour] += 1
    armour_inventory[armour] -= 1
    equipped_armour = armour

def UseHealing(healing_item):
    global player_max_health
    global player_health
    if player_health + healing_amount_index.get(healing_item) > player_max_health:
        temp = player_health + healing_amount_index.get(healing_item)
        difference = player_max_health - temp
        player_health = player_max_health
        print(f"\nThe {healing_item} healed you to full health. Your health is now {player_health}. (Healed {(healing_amount_index.get(healing_item) + difference)} health)\n\n———————————————————————————————————————————\n")
        HealingMenu()
    else:
        player_health += healing_amount_index.get(healing_item)
        print(f"\nYou used the {healing_item}. Your health is now {player_health}. (Healed {healing_amount_index.get(healing_item)} health)\n\n———————————————————————————————————————————\n")
        HealingMenu()
    
def CheckWeapon(weapon):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{weapon}: {weapon_damage_index.get(weapon)} ATK\n\n“{weapon_description_index.get(weapon)}”\n")
            print("   1. Equip Weapon\n   2. Back to Weapons Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!")
        else:
            if decision == 1:
                player_action_taken = True
                EquipWeapon(weapon)
                WeaponsMenu()
            elif decision == 2:
                player_action_taken = True
                WeaponsMenu()
            else:
                print("Please enter a valid number!")
                

        
def CheckHealing(healing_item):
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n{healing_item}: {healing_amount_index.get(healing_item)} HEAL\n\n“{healing_description_index.get(healing_item)}”\n")
            print("   1. Use Healing Item\n   2. Back to Healing Items Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!")
        else:
            if decision == 1:
                player_action_taken = True
                UseHealing(healing_item)
            elif decision == 2:
                player_action_taken = True
                HealingMenu()
            else:
                print("Please enter a valid number!")
            
            
def CheckArmour():
    return

def CheckKeyItem():
    return



def WeaponsMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
            try:
                print("\n1. Weapons Menu\n")
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
                print(f"\n   {i}. Back to Bag Menu\n\n———————————————————————————————————————————\n")
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
            elif  decision > len(healing_list):
                print("Please enter a valid number!\n")
            elif healing_amount_list[decision - 1] == 0:
                print("Please enter a valid number!\n")
            else:
                for healing_item in healing_list:
                    if decision == (healing_list.index(healing_item)+ 1):
                        player_action_taken = True 
                        CheckHealing(healing_item)



        

def ArmourMenu():
    return

def KeyItemsMenu():
    return

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
                print(f"   1. Move East (Positive X), [X:{x+1}, Y:{y}] - “{tile_map.get((x+1,y)).get("Name")}”") 
            except AttributeError:
                print(f"   1. Move East (Positive X), [X:{x+1}, Y:{y}] - “Obstructed”")
                east_tile = "invalid"
            try:
                print(f"   2. Move West (Negative X), [X:{x-1}], Y:{y}] - “{tile_map.get((x-1,y)).get("Name")}”") 
            except AttributeError:
                print(f"   2. Move West (Negative X), [X:{x-1}], Y:{y}] - “Obstructed”")
                west_tile = "invalid"
            try: 
                print(f"   3. Move North (Positive Y) [X:{x}, Y:{y+1}] - “{tile_map.get((x,y+1)).get("Name")}”") 
            except AttributeError:
                print(f"   3. Move North (Positive Y) [X:{x}, Y:{y+1}] - “Obstructed”")
                north_tile = "invalid"
            try: 
                print(f"   4. Move South (Negative Y) [X:{x}, Y:{y-1}] - “{tile_map.get((x,y-1)).get("Name")}”\n")
            except AttributeError:
                print(f"   4. Move South (Negative Y) [X:{x}, Y:{y-1}] - “Obstructed”\n")
            print("   5. Back to Menu\n\n———————————————————————————————————————————\n")
            decision = int(input())
            
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1 and east_tile != "invalid":
                player_action_taken = True 
                print(f"\nYou have moved East. [X:{x+1}, Y:{y}] - “{tile_map.get((x+1,y)).get("Name")}”")
                player_pos = (x+1, y)
                ExplorationScreen(*player_pos)
            elif decision == 1 and east_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 2 and west_tile != "invalid":
                player_action_taken = True
                print(f"\nYou have moved West. [X:{x-1}, Y:{y}] - “{tile_map.get((x-1,y)).get("Name")}”")
                player_pos = (x-1, y)
                ExplorationScreen(*player_pos)
            elif decision == 2 and west_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 3 and north_tile != "invalid":
                player_action_taken = True
                print(f"\nYou have moved North. [X:{x}, Y:{y+1}] - “{tile_map.get((x,y+1)).get("Name")}”")
                player_pos = (x, y+1)
                ExplorationScreen(*player_pos)
            elif decision == 3 and north_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 4 and south_tile != "invalid":
                player_action_taken = True
                print(f"\nYou have moved South. [X:{x}, Y:{y-1}] - “{tile_map.get((x,y-1)).get("Name")}")
                player_pos = (x, y-1)
                ExplorationScreen(*player_pos)
            elif decision == 4 and south_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 5:
                player_action_taken = True
                ExplorationScreen(*player_pos)
            else:
                print("Please enter a valid number!\n")


def Interaction(x,y):
    tile_map.get((x,y)).update({"Interacted": True})
    print("interaction now true, update this variable you silly")



def ExplorationScreen(x,y):
    
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\nHero  [—————]  [X:{x}, Y:{y}] - {tile_map.get((x,y)).get("Name")}, {tile_map.get((x,y)).get("Location")}\n\n“{tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {tile_map.get((x,y)).get("Type")}\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if decision == 1 and tile_map.get((x,y)).get("Type") == "Interact":
                Interaction(x,y)
            elif decision == 1 and tile_map.get((x,y)).get("Type") == "Battle":
                if tile_map.get((x,y)).get("Battle Complete") == "True":
                    print("You have already completed this battle!")
                if tile_map.get((x,y)).get("Battle Complete") == "False":
                    # Battle(creature, level)
                    return
            elif decision == 1 and tile_map.get((x,y)).get("Type") == "Shop":
                # Shop Menu 
                return
            elif decision == 1 and tile_map.get((x,y)).get("Type") == "Item":
                # Item obtained
                return

            elif decision == 2:
                MovementMenu(x,y)
                player_action_taken = True
            elif decision == 3:
                BagMenu()
                player_action_taken = True
            else:
                print("Please enter a valid number!\n")




StartSequence()

ExplorationScreen(*player_pos)


