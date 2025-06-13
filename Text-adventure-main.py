player_pos = 1,0
player_alive = True

def StartSequence():
    return



tile_map = {
    
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

# weapon indexes (update to one biiig dict if you wanna :3)
weapon_damage_index = {
    "Training Sword": 30,
    "Master Sword": 300,
}

healing_point_index = {
    "Potion": 5,
    "Elixr": 10,
    "Shimmering Potion": 20,
    "Good healing item": 50,
}

weapon_inventory = {
    "Training Sword": 1,
    "Greatsword": 3,
    "Master Sword": 0,
}

healing_inventory = ["Potion", "Elixir", "Potion"]
armour_inventory = []
key_item_inventory = []

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
                            print(f"{i}. {weapon} (x{weapon_amount_list[weapon_list.index(weapon)]}) ")
                            i += 1
                        elif weapon_amount_list[weapon_list.index(weapon)] == 1:
                            print(f"{i}. {weapon}")
                            i += 1
                decision = int(input())
            except ValueError: 
                print("Please enter a valid number!")
            else:
                        
                if decision - 1 > len(weapon_list):
                    print("Please enter a valid number!")
                elif weapon_amount_list[decision - 1] == 0:
                    print("Please enter a valid number!")
                else:
                    for weapon in weapon_list:
                        if decision == (weapon_list.index(weapon) + 1):
                            print(weapon) ## function
                            player_action_taken = True
                
                
                
                
                
                
            
            # for weapon in weapon_inventory:
            #     print(f"    {(weapon_inventory.index(weapon))}. {weapon}")
            player_action_taken = True
        # except ValueError:
        #     print("Please enter a valid number!")


def HealingMenu():
    return

def ArmourMenu():
    return

def KeyItemsMenu():
    return

def BagMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:

        try:
            print("\n3. Bag Menu\n\n Which pocket would you like to inspect?\n\n  1. Weaponry\n   2. Medicine\n   3. Key Items")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!")
        else:
            if decision == 1:
                WeaponsMenu()
                player_action_taken = True
            elif decision == 2:
                HealingMenu()
                player_action_taken = True
            elif decision == 3:
                ArmourMenu()
                player_action_taken = True
            elif decision == 4:
                KeyItemsMenu()
                player_action_taken = True
            else:
                print("Please enter a valid number!")
            




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
                print(f"    1. Move East (Positive X), [X:{x+1}, Y:{y}] - “{tile_map.get((x+1,y)).get("Name")}”") 
            except AttributeError:
                print(f"    1. Move East (Positive X), [X:{x+1}, Y:{y}] - “Obstructed”")
                east_tile = "invalid"
            try:
                print(f"    2. Move West (Negative X), [X:{x-1}], Y:{y}] - “{tile_map.get((x-1,y)).get("Name")}”") 
            except AttributeError:
                print(f"    2. Move West (Negative X), [X:{x-1}], Y:{y}] - “Obstructed”")
                west_tile = "invalid"
            try: 
                print(f"    3. Move North (Positive Y) [X:{x}, Y:{y+1}] - “{tile_map.get((x,y+1)).get("Name")}”") 
            except AttributeError:
                print(f"    3. Move North (Positive Y) [X:{x}, Y:{y+1}] - “Obstructed”")
                north_tile = "invalid"
            try: 
                print(f"    4. Move South (Negative Y) [X:{x}, Y:{y-1}] - “{tile_map.get((x,y-1)).get("Name")}”\n")
            except AttributeError:
                print(f"    4. Move South (Negative Y) [X:{x}, Y:{y-1}] - “Obstructed”\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!")
        else:
            if decision == 1 and east_tile != "invalid":
                print(f"You have moved East. [X:{x+1}, Y:{y}] - “{tile_map.get((x+1,y)).get("Name")}”")
                player_pos = (x+1, y)
                player_action_taken = True 
            elif decision == 1 and east_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 2 and west_tile != "invalid":
                print(f"You have moved West. [X:{x-1}, Y:{y}] - “{tile_map.get((x-1,y)).get("Name")}”")
                
                player_pos = (x-1, y)
                player_action_taken = True
            elif decision == 2 and west_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 3 and north_tile != "invalid":
                print(f"You have moved North. [X:{x}, Y:{y+1}] - “{tile_map.get((x,y+1)).get("Name")}”")
                player_pos = (x, y+1)
                player_action_taken = True
            elif decision == 3 and north_tile == "invalid":
                print("This tile is obstructed!")
            elif decision == 4 and south_tile != "invalid":
                print(f"You have moved South. [X:{x}, Y:{y-1}] - “{tile_map.get((x,y-1)).get("Name")}")
                player_pos = (x, y-1)
                player_action_taken = True
            elif decision == 4 and south_tile == "invalid":
                print("This tile is obstructed!")
            else:
                print("Please enter a valid number!")


def Interaction(x,y):
    tile_map.get((x,y)).update({"Interacted": True})
    print("interaction now true, update this variable you silly")



def ExplorationScreen(x,y):
    
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"Hero  [—————]  [X:{x}, Y:{y}] - {tile_map.get((x,y)).get("Name")}, {tile_map.get((x,y)).get("Location")}\n\n“{tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {tile_map.get((x,y)).get("Type")}\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            decision = int(input())
        except ValueError:
            print("Please enter a valid number!")
        else:
            if decision == 1 and tile_map.get((x,y)).get("Type") == "Interact":
                Interaction(x,y)
            elif decision == 1 and tile_map.get((x,y)).get("Type") == "Battle":
                if tile_map.get((x,y)).get("Battle Complete") == "True":
                    print("You have already completed this battle!")
                if tile_map.get((x,y)).get("Battle Complete") == "False":
                    # Battle(creature, level)
                    return

            elif decision == 2:
                MovementMenu(x,y)
                player_action_taken = True
            elif decision == 3:
                BagMenu()
                player_action_taken = True
            else:
                print("Please enter a valid number!")




StartSequence()

ExplorationScreen(*player_pos)


