import world_map
import random

# main player values 
player_pos = 16, 32 # handles the position on the map in (x,y)
player_max_health = 100 #
player_health = 100
player_gold = 10

# Start and ending sequences for the game 
def StartSequence():
    global player_name
    print("Foreword: \n\nWelcome to my silly little project! No data fromt his program is stored anywhere, and it is not malicious.\nFor more info and help with the RPG, such as a provided map, please refer to the README that should have came with this script.\nThis script also depends on the 'world_map.py' script which also should have came with this file. \nIf you're missing either of these files, this script may be compromised and I advise you to proceed at your own risk.\n")
    
    print("The goal of your quest is to travel through the map and slay the Elder Dragon.\n")

    player_name = input("Adventurer, what is your name?\n\n").title()
    # Unpacks the tuple, so the code can actually run
    ExplorationScreen(*player_pos)




def EndingSequence(Ending):
    global player_name
    if Ending == "Bad Ending":
        print(f"\n“Sadly, {player_name} takes a lethal blow to the head in battle. Better luck next time...”\n\nThank you for playing my game !! <3\n- Alex")
        print("Quitting script..\n")
        quit()
    elif Ending == "Bad Boss Ending":
        print(f"\n“{player_name}, don't lose hope! Stay determined! Better luck next time...”\n\nThank you for playing my game !! <3\n- Alex\n")
        print("Quitting script..\n")
        quit()
    elif Ending == "Good Ending":
        print(f"\n“{player_name} has successfully slain the Elder Dragon and completed their quest. Great Job!”\n\nThank you for playing my game !! <3\n- Alex\n")
        print("Quitting script..\n")
        quit()
    




# inventory indexes for the player - value is how many in inventory, the comments beside them are what area these items are related to.
weapon_inventory = {
    "Training Sword": 1,   # Kingdom Outskirts
    "Thornblade": 1,   # Verdant Forest
    "Crystal Dagger": 1,   # Shimmering Cave
    "Shard Of Glass": 1,   # The Desert
    "Twin Daggers": 1,   # Howling Cliffs
}

healing_inventory = {
    "Pocket Spell Jar": 1,   # Kingdom Outskirts
    "Elixir": 2,   # Verdant Forest
    "Shimmering Potion": 3,   # Shimmering Cave
    "Tarnished Locket": 1,   # The Desert
    "Lightning Brew": 2,   # Howling Cliffs
}
armour_inventory = {
    "Leather Armour": 0,    # Kingdom Outskirts
    "Chainmail": 0,   # Verdant Forest
    "Unusual Cloak": 0,   # Shimmering Cave
    "Sandstorm Gear": 0,   # The Desert
    "Cult Robes": 1,   # Howling Cliffs
}
key_items_inventory = {
    "Sacred Sigil Of Flame": 0,   # The Desert
    "Ancient Key": 0,   # Howling Cliffs 
}

# description indexes - these appear when 'checking' the item in the bag menu. 

weapon_description_index = {
    "Training Sword": "A basic training sword. There were hundreds of these things lying around your hometown. Enough to protect yourself, but not much else.",
    "Thornblade": "A blade uprooted from a bed of thorns. Effective, but the thorns wrapped around the handle certainly make it difficult to use.",
    "Crystal Dagger": "A sharp, crystalline dagger which sparkles brightly.", 
    "Shard Of Glass": "A shard of glass from a an ancient artefact. Mirages of riches can be seen in its reflection.",
    "Twin Daggers": "Sometimes you think you can hear these daggers whispering to each other.",
    
}

healing_description_index = {
    "Pocket Spell Jar": "Filled with an assortment of bright herbs. The cork stopper has melted over the jar.",
    "Elixir": "An elixir that was said to bring eternal youth. Tastes nice.",
    "Shimmering Potion": "Swirling, bright purple liquid is visible despite the potion's dark, dusty exterior. You question whether this would be a great thing to drink.",
    "Tarnished Locket": "A locket with a faded photograph of someone you do not recognise.",  
    "Lightning Brew": "An incredibly strong ale. It sparks as it fizzes.",
}

armour_description_index = {
    "Leather Armour": "A comfortable, well-made set of leather armour.",   
    "Chainmail": "A heavier armour set which makes you feel sluggish.",   
    "Unusual Cloak": "This cloak's fibers feel very.. unique. You have heard rumours about cloaks forged from ancient mythological creatures, and you wonder if this could be one of them.",  
    "Sandstorm Gear": "Gear fit for a sandstorm, with goggles and covered clothes. Seems strangely high-tech. Faint whirring sounds can be heard from the goggles.",
    "Cult Robes": "Robes emanating an otherworldly power. What on earth happened up in these cliffs?", 
}

key_item_description_index = {
    "Sacred Sigil Of Flame": "Inscribed with the words 'Sigil of Flame'. Despite being in the middle of a desert, it is still in perfect condition.",
    "Ancient Key": "An ancient, heavy key. It feels very, very familiar."

}


# Value indexes for statistics actually used in the game - pretty straightforward.

weapon_damage_index = {
    "Training Sword": 5,   # Kingdom Outskirts
    "Thornblade": 8,   # Verdant Forest
    "Crystal Dagger": 12,   # Shimmering Cave
    "Shard Of Glass": 14,   # The Desert
    "Twin Daggers": 18,   # Howling Cliffs
}

healing_amount_index = {
    "Pocket Spell Jar": 5,   # Kingdom Outskirts
    "Elixir": 10,   # Verdant Forest
    "Shimmering Potion": 20,   # Shimmering Cave
    "Tarnished Locket": 50,   # The Desert
    "Lightning Brew": 100,   # Howling Cliffs
}

armour_reduction_index = {
    "Leather Armour": 2,    # Kingdom Outskirts
    "Chainmail": 4,   # Verdant Forest
    "Unusual Cloak": 6,   # Shimmering Cave
    "Sandstorm Gear": 8,   # The Desert
    "Cult Robes": 10,   # Howling Cliffs
}


# Price index for purchasing items - if it was within the scope selling could be possible using these indexes too.

weapon_price_index = {
    "Training Sword": 10,  
    "Thornblade": 25,   # Verdant Forest
    "Crystal Dagger": 50,   # Shimmering Cave
    "Shard Of Glass": 70,   # The Desert
    "Twin Daggers": 100,   # Howling Cliffs
}

healing_price_index = {
    "Pocket Spell Jar": 5,   # Kingdom Outskirts
    "Elixir": 12,   # Verdant Forest
    "Shimmering Potion": 25,   # Shimmering Cave
    "Tarnished Locket": 40,   # The Desert
    "Lightning Brew": 100,   # Howling Cliffs
}

armour_price_index = {
    "Leather Armour": 15,    # Kingdom Outskirts
    "Chainmail": 35,   # Verdant Forest
    "Unusual Cloak": 60,   # Shimmering Cave
    "Sandstorm Gear": 80,   # The Desert
    "Cult Robes": 110,   # Howling Cliffs
}

equipped_weapon = "Training Sword"
equipped_armour = "Leather Armour"

# Battle System dictionaries

# A list for the various states of the enemy/player healthbars for visual clarity.
healthbar_ui = ["[          ]","[-         ]","[--        ]","[---       ]","[----      ]","[-----     ]","[------    ]","[-------   ]","[--------  ]","[--------- ]", "[----------]"]

# The index of which monsters can be encountered, each with their own stats. These are based on area of the game.
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
    "Verdant Forest": {
        "Forest Sprite": {
            "Max Damage": 8,
            "Min Damage": 4,
            "Max Health": 22,
            "Min Health": 12,
            "Accuracy": 90,
        },
        "Violent Sapling": {
            "Max Damage": 11,
            "Min Damage": 6,
            "Max Health": 28,
            "Min Health": 18,
            "Accuracy": 65,
        },
        "Poison Toad": {
            "Max Damage": 9,
            "Min Damage": 3,
            "Max Health": 20,
            "Min Health": 10,
            "Accuracy": 75,
        }
    },
    "Shimmering Cave": {
        "Crystal Golem": {
            "Max Damage": 15,
            "Min Damage": 9,
            "Max Health": 45,
            "Min Health": 30,
            "Accuracy": 60,
        },
        "Echo Bat": {
            "Max Damage": 11,
            "Min Damage": 5,
            "Max Health": 22,
            "Min Health": 14,
            "Accuracy": 85,
        },
        "Wisp": {
            "Max Damage": 12,
            "Min Damage": 7,
            "Max Health": 28,
            "Min Health": 16,
            "Accuracy": 80,
        }
    },
    "The Desert": {
        "Sandworm": {
            "Max Damage": 16,
            "Min Damage": 10,
            "Max Health": 40,
            "Min Health": 25,
            "Accuracy": 70,
        },
        "Scorch Beetle": {
            "Max Damage": 13,
            "Min Damage": 6,
            "Max Health": 26,
            "Min Health": 15,
            "Accuracy": 75,
        },
        "Dust Phantom": {
            "Max Damage": 14,
            "Min Damage": 8,
            "Max Health": 32,
            "Min Health": 20,
            "Accuracy": 85,
        }
    },
    "Howling Cliffs": {
        "Harpy": {
            "Max Damage": 18,
            "Min Damage": 10,
            "Max Health": 36,
            "Min Health": 22,
            "Accuracy": 90,
        },
        "Cliff Stalker": {
            "Max Damage": 17,
            "Min Damage": 9,
            "Max Health": 30,
            "Min Health": 20,
            "Accuracy": 95,
        },
        "Storm Revenant": {
            "Max Damage": 20,
            "Min Damage": 12,
            "Max Health": 48,
            "Min Health": 30,
            "Accuracy": 85,
        }
    },
    "The Peak": {
        "Elder Dragon": {
            "Max Damage": 35,
            "Min Damage": 20,
            "Max Health": 200,
            "Min Health": 200,
            "Accuracy": 80,
        }, 
    },
}


#Functions below this point are used for the core game 


# Equips weapon/armour
def EquipWeapon(weapon):
    global equipped_weapon
    print(f"\nYou have equipped {weapon}. Your previous weapon was the {equipped_weapon}.\n\n———————————————————————————————————————————\n")
    # Adds previous weapon to inventory and removes newly equipped weapon
    weapon_inventory[equipped_weapon] += 1
    weapon_inventory[weapon] -= 1
    equipped_weapon = weapon

def EquipArmour(armour):
    global equipped_armour
    print(f"\nYou have equipped {armour}. Your previous armour was {equipped_armour}.\n\n———————————————————————————————————————————\n")
    # Adds previous armour to inventory and removes newly equipped armour
    armour_inventory[equipped_armour] += 1
    armour_inventory[armour] -= 1
    equipped_armour = armour

def UseHealing(healing_item):
    global player_max_health
    global player_health
    # Checks first to see fi the player is at full health, not wasting a potion.
    if player_health == player_max_health:
        print(f"\nThe {healing_item} will not have any effect! The {healing_item} was not consumed.")
        HealingMenu()
    # Then checks if the potion will go over full health, to handle this case
    elif player_health + healing_amount_index.get(healing_item) > player_max_health:
        temp = player_health + healing_amount_index.get(healing_item)
        difference = player_max_health - temp
        player_health = player_max_health
        print(f"\nThe {healing_item} healed you to full health. Your health is now {player_health}. (Healed {(healing_amount_index.get(healing_item) + difference)} health)\n\n———————————————————————————————————————————\n")
        healing_inventory[healing_item] -= 1
        HealingMenu()
    # Otherwise, just simply add health back to the player
    else:
        player_health += healing_amount_index.get(healing_item)
        print(f"\nYou used the {healing_item}. Your health is now {player_health}. (Healed {healing_amount_index.get(healing_item)} health)\n\n———————————————————————————————————————————\n")
        healing_inventory[healing_item] -= 1
    

# Check Items to display descriptions on them. Also used as a link to equip/use items in the above menu. 
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
                # Runs the equip process, then returns to main weapons list 
                player_action_taken = True
                EquipWeapon(weapon)
                WeaponsMenu()
            elif decision == 2:
                # Just returns to main weapons list 
                player_action_taken = True
                WeaponsMenu()
            else:
                print("Please enter a valid number!\n")
                


# Exactly the same as above funtion, for healing
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
            

# Exactly the same as above function, for armour
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
            

# Cannot equip/do anything with key items, so display a slightly different menu with no equip/use option
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




# Situatonal Shop Menu for when the player is on a shop tile
def ShopMenu(x,y):
    # Uses global variables to manipulate the player inventory and gold amount
    global player_gold
    global weapon_inventory
    global healing_inventory
    global armour_inventory
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"{world_map.tile_map.get((x,y)).get("Name")}: Shop Menu - {player_gold} Gold\n")
            i = 1
            # Get the shop contents based on postion and display them in a list
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
            # If the decision is the last number, it is the 'back' option. Send the player back to menu.
            if decision == i:
                player_action_taken = True
                ExplorationScreen(x,y)
            # Checking for boundary cases
            elif decision > len(world_map.tile_map.get((x,y)).get("Shop Contents")):
                    print("Please enter a valid number!\n")
            # Attempt to buy item
            else:
                 for item in world_map.tile_map.get((x,y)).get("Shop Contents"):
                    if decision == (world_map.tile_map.get((x,y)).get("Shop Contents").index(item) + 1):
                        # These shouldnt be in separate dictionaries, but because they are, check through all of them for the item
                        if item in weapon_price_index:
                            # Check if player has enough gold 
                            if player_gold - weapon_price_index[item] < 0:
                                # The player does not have enough gold, so it returns to the menu
                                player_action_taken = True
                                print(f"You do not have enough money! This item costs {weapon_price_index.get(item)} Gold but you only have {player_gold} Gold!\n")
                                ShopMenu(x,y)
                            # Else, they do have enough gold, subtract the cost of the item and add one copy of the item to inventory
                            else:
                                player_action_taken = True
                                player_gold -= weapon_price_index.get(item)
                                weapon_inventory[item] += 1
                                print(f"You have purchased the {item}, which cost {weapon_price_index.get(item)} Gold. Your new balance is {player_gold} Gold.\n")
                                ShopMenu(x,y)
                        # Check if player has enough gold 
                        elif item in healing_price_index:
                            # The player does not have enough gold, so it returns to the menu
                            if player_gold - healing_price_index[item] < 0:
                                player_action_taken = True
                                print(f"You do not have enough money! This item costs {healing_price_index.get(item)} Gold but you only have {player_gold} Gold!\n")
                                ShopMenu(x,y)
                            # Else, they do have enough gold, subtract the cost of the item and add one copy of the item to inventory
                            else:
                                player_action_taken = True
                                player_gold -= healing_price_index.get(item)
                                healing_inventory[item] += 1
                                print(f"You have purchased the {item}, which cost {healing_price_index.get(item)} Gold. Your new balance is {player_gold} Gold.\n")
                                ShopMenu(x,y)
                        # Check if player has enough gold 
                        elif item in armour_price_index:
                            # The player does not have enough gold, so it returns to the menu
                            if player_gold - armour_price_index[item] < 0:
                                player_action_taken = True
                                print(f"You do not have enough money! This item costs {armour_price_index.get(item)} Gold but you only have {player_gold} Gold!\n")
                                ShopMenu(x,y)
                            # Else, they do have enough gold, subtract the cost of the item and add one copy of the item to inventory
                            else:
                                player_action_taken = True
                                player_gold -= armour_price_index.get(item)
                                armour_inventory[item] += 1
                                print(f"You have purchased the {item}, which cost {armour_price_index.get(item)} Gold. Your new balance is {player_gold} Gold.\n")
                                ShopMenu(x,y)

# Core Menus inside of Bag menu - leading to the deeper listed functions
def WeaponsMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
            try:
                print(f"\n1. Weapons Menu: {equipped_weapon} currently equipped\n")
                # Makes weapon inventory dict into a list so it can be displayed 
                weapon_list = list(weapon_inventory)
                weapon_amount_list = list(weapon_inventory.values())
                i = 1
                available_weapon_list = []
                # Prints out all weapons in list (Format differently based on how many are in inventory)
                for weapon in weapon_list:
                        if weapon_amount_list[weapon_list.index(weapon)] > 1:
                            print(f"   {i}. {weapon} (x{weapon_amount_list[weapon_list.index(weapon)]})")
                            available_weapon_list.append(weapon)
                            i += 1
                        elif weapon_amount_list[weapon_list.index(weapon)] == 1:
                            print(f"   {i}. {weapon}")
                            available_weapon_list.append(weapon)
                            i += 1
                print(f"\n   {i}.  Back to Bag Menu\n\n———————————————————————————————————————————\n")
                decision = int(input())
            # Handle cases where a number is not entered 
            except ValueError: 
                print("Please enter a valid number!\n")
            # If it does not fail, then the else can run
            else:
                if decision == i:
                    player_action_taken = True
                    BagMenu()
                # Bounary case for a number outside of the list
                elif decision > len(weapon_list):
                    print("Please enter a valid number!\n")
                else:
                    for weapon in available_weapon_list:
                        if decision == (available_weapon_list.index(weapon) + 1):
                            player_action_taken = True
                            CheckWeapon(weapon)
                            
#Identical to to previous menu, but for healing 
def HealingMenu():
    decision = 0 
    player_action_taken = False
    while player_action_taken == False:
        try:
            print("\n2. Healing Menu\n")
            healing_list = list(healing_inventory)
            healing_amount_list = list(healing_inventory.values())
            i = 1 
            available_healing_list = []
            for healing_item in healing_list:
                if healing_amount_list[healing_list.index(healing_item)] > 1:
                    print(f"   {i}. {healing_item} (x{healing_amount_list[healing_list.index(healing_item)]})")
                    available_healing_list.append(healing_item)
                    i += 1
                elif healing_amount_list[healing_list.index(healing_item)] == 1:
                    print(f"   {i}. {healing_item}")
                    available_healing_list.append(healing_item)
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
            else:
                for healing_item in available_healing_list:
                    if decision == (available_healing_list.index(healing_item)+ 1):
                        player_action_taken = True 
                        CheckHealing(healing_item)



# Identical to to previous menu, but for armour
def ArmourMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print(f"\n3. Armour Menu: {equipped_armour} currently equipped\n")
            armour_list = list(armour_inventory)
            armour_amount_list = list(armour_inventory.values())
            i = 1
            available_armour_list = []
            for armour in armour_list:
                if armour_amount_list[armour_list.index(armour)] > 1:
                    print(f"   {i}. {armour} (x{armour_amount_list[armour_list.index(armour)]})")
                    available_armour_list.append(armour)
                    i += 1
                elif armour_amount_list[armour_list.index(armour)] == 1:
                    print(f"   {i}. {armour}")
                    available_armour_list.append(armour)
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
            else:
                for armour in available_armour_list:
                    if decision == (available_armour_list.index(armour)+ 1):
                        player_action_taken = True 
                        CheckArmour(armour)



# Identical to previous menu, but for key items
def KeyItemsMenu():
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            print("\n4. Key Items Menu\n")
            key_items_list = list(key_items_inventory)
            key_items_amount_list = list(key_items_inventory.values())
            i = 1
            available_key_items_list = []
            for key_item in key_items_list:
                print(f"   {i}. {key_item}")
                available_key_items_list.append(key_item)
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
            else:
                for key_item in available_key_items_list:
                    if decision == (available_key_items_list.index(key_item)+ 1):
                        player_action_taken = True 
                        CheckKeyItem(key_item)


# Basic bag menu, used to look at any pocket of the bag. Same logic as other menus.
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
            



# Movement menu for the movement systems.
def MovementMenu(x,y):
    global player_pos
    decision = 0
    player_action_taken = False
    # Checks if the tile is uncompleted and a battle tile, denying movement if so
    if world_map.tile_map.get((x,y)).get("Type") == "Battle" and world_map.tile_map.get((x,y)).get("Battle Complete") == False:
        print("\nYou cannot move from an uncompleted Battle Tile!")
        ExplorationScreen(x,y)
    else:
        while player_action_taken == False: 
            try:
                # Due to attribute errors, these are all separate try blocks
                # Variables for determining tile eiligibility
                east_tile = None
                west_tile = None
                north_tile = None 
                south_tile = None
                print(f"\n2. Movement Menu - (X:{x},Y:{y})\n")
                try:
                    print(f"   1. Move East (Positive X), [X:{x+1}, Y:{y}] - {world_map.tile_map.get((x+1,y)).get("Type")} Tile: “{world_map.tile_map.get((x+1,y)).get("Name")}”") 
                except AttributeError:
                    print(f"   1. Move East (Positive X), [X:{x+1}, Y:{y}] - Obstructed")
                    east_tile = "invalid"
                try:
                    print(f"   2. Move West (Negative X), [X:{x-1}], Y:{y}] - {world_map.tile_map.get((x-1,y)).get("Type")} Tile: “{world_map.tile_map.get((x-1,y)).get("Name")}”") 
                except AttributeError:
                    print(f"   2. Move West (Negative X), [X:{x-1}], Y:{y}] - Obstructed")
                    west_tile = "invalid"
                try: 
                    print(f"   3. Move North (Positive Y) [X:{x}, Y:{y+1}] - {world_map.tile_map.get((x,y+1)).get("Type")} Tile: “{world_map.tile_map.get((x,y+1)).get("Name")}”") 
                except AttributeError:
                    print(f"   3. Move North (Positive Y) [X:{x}, Y:{y+1}] - Obstructed")
                    north_tile = "invalid"
                try: 
                    print(f"   4. Move South (Negative Y) [X:{x}, Y:{y-1}] - {world_map.tile_map.get((x,y-1)).get("Type")} Tile: “{world_map.tile_map.get((x,y-1)).get("Name")}”") 
                except AttributeError:
                    print(f"   4. Move South (Negative Y) [X:{x}, Y:{y-1}] - Obstructed\n")
                    south_tile = "invalid"
                print("   5. Back to Menu\n\n———————————————————————————————————————————\n")
                
                decision = int(input())
            
            except ValueError:
                print("Please enter a valid number!\n")
            else:
                # Another standard conditional check system, checks if tile selected is invalid
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
                # Make sure the player cannot move through locked tiles
                elif decision == 3 and world_map.tile_map.get((x,y)).get("Type") == "Gate":
                    if world_map.tile_map.get((x,y)).get("Unlocked") == False:
                        print("\nThis tile is obstructed! You must unlock this gate first!")
                    else:
                        player_action_taken = True
                        print(f"\nYou have moved North. [X:{x}, Y:{y+1}] - {world_map.tile_map.get((x,y+1)).get("Type")} Tile: “{world_map.tile_map.get((x,y+1)).get("Name")}”")
                        player_pos = (x, y+1)
                        ExplorationScreen(*player_pos)
                elif decision == 3 and north_tile != "invalid":
                    player_action_taken = True
                    print(f"\nYou have moved North. [X:{x}, Y:{y+1}] - {world_map.tile_map.get((x,y+1)).get("Type")} Tile: “{world_map.tile_map.get((x,y+1)).get("Name")}”")
                    player_pos = (x, y+1)
                    ExplorationScreen(*player_pos)
                elif decision == 3 and north_tile == "invalid":
                    print("\nThis tile is obstructed!")
                elif decision == 4 and south_tile != "invalid":
                    player_action_taken = True
                    print(f"\nYou have moved South. [X:{x}, Y:{y-1}] - {world_map.tile_map.get((x,y-1)).get("Type")} Tile: “{world_map.tile_map.get((x,y-1)).get("Name")}”")
                    player_pos = (x, y-1)
                    ExplorationScreen(*player_pos)
                elif decision == 4 and south_tile == "invalid":
                    print("\nThis tile is obstructed!")
                elif decision == 5:
                    player_action_taken = True
                    ExplorationScreen(*player_pos)
                else:
                    print("Please enter a valid number!\n")

# Interaction menu to obtain items 
def Interaction(x,y):
    # Displays a different message if reward is already obtained, so the player cannot get infinite items
    if world_map.tile_map.get((x,y)).get("Reward Obtained") == True:
        print("Reward has already been obtained!\n\n———————————————————————————————————————————\n")
        ExplorationScreen(x,y)
    elif world_map.tile_map.get((x,y)).get("Reward Obtained") == False:
        print(f"\n“{world_map.tile_map.get((x,y)).get("Interaction Text")}.”\n")
    # Same system for displaying if the reward is singular or multiple
        world_map.tile_map.get((x,y)).update({"Reward Obtained": True})
        if world_map.tile_map.get((x,y)).get("Reward Amount") == 1:
            print(f"You found a {world_map.tile_map.get((x,y)).get("Reward")}.")
            if world_map.tile_map.get((x,y)).get("Reward") in weapon_inventory:
                weapon_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
            elif world_map.tile_map.get((x,y)).get("Reward") in healing_inventory:
                healing_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
            elif world_map.tile_map.get((x,y)).get("Reward") in  armour_inventory:
                armour_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
            elif world_map.tile_map.get((x,y)).get("Reward") in key_items_inventory:
                key_items_inventory[world_map.tile_map.get((x,y)).get("Reward")] += 1
        else:
            print(f"You found a {world_map.tile_map.get((x,y)).get("Reward")} (x{world_map.tile_map.get((x,y)).get("Reward Amount")}).")
            if world_map.tile_map.get((x,y)).get("Reward") in weapon_inventory:
                weapon_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
            elif world_map.tile_map.get((x,y)).get("Reward") in healing_inventory:
                healing_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
            elif world_map.tile_map.get((x,y)).get("Reward") in  armour_inventory:
                armour_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
            elif world_map.tile_map.get((x,y)).get("Reward") in key_items_inventory:
                key_items_inventory[world_map.tile_map.get((x,y)).get("Reward")] += world_map.tile_map.get((x,y)).get("Reward Amount")
        print("\n———————————————————————————————————————————\n")
        ExplorationScreen(x,y)

# Slightly tweaked healing scripts for during an encounter 
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
                return UseBattleHealing(healing_item) # Boolean variable 

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
            available_healing_list = []
            for healing_item in healing_list:
                if healing_amount_list[healing_list.index(healing_item)] > 1:
                    print(f"   {i}. {healing_item} (x{healing_amount_list[healing_list.index(healing_item)]})")
                    available_healing_list.append(healing_item)
                    i += 1
                elif healing_amount_list[healing_list.index(healing_item)] == 1:
                    print(f"   {i}. {healing_item}")
                    available_healing_list.append(healing_item)
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
                for healing_item in available_healing_list:
                    if decision == (available_healing_list.index(healing_item)+ 1):
                        player_action_taken = True 
                        return CheckBattleHealing(healing_item) # True/false boolean


#Encounter System used on Battle tiles - could certainly be more efficient.
def EnemyEncounter(x,y):
    global player_max_health
    global player_health
    global player_gold

    player_damage = weapon_damage_index[equipped_weapon]
    player_damage_reduction = armour_reduction_index[equipped_armour]
    
 
# decides on monster type - gets a random one based on area of encounter
# It's inefficient, I know - but gets the job done 

    if world_map.tile_map.get((x,y)).get("Location") == "Kingdom Outskirts":
        monster_list = list(monster_index.get("Kingdom Outskirts"))
        monster = random.choice(monster_list)
        monster_max_hp = random.randint(monster_index.get("Kingdom Outskirts").get(monster).get("Min Health"), monster_index.get("Kingdom Outskirts").get(monster).get("Max Health"))
        monster_accuracy = monster_index.get("Kingdom Outskirts").get(monster).get("Accuracy")
        monster_min_damage = monster_index.get("Kingdom Outskirts").get(monster).get("Min Damage")
        monster_max_damage = monster_index.get("Kingdom Outskirts").get(monster).get("Max Damage")
    
    elif world_map.tile_map.get((x,y)).get("Location") == "Verdant Forest":
        monster_list = list(monster_index.get("Verdant Forest"))
        monster = random.choice(monster_list)
        monster_max_hp = random.randint(monster_index.get("Verdant Forest").get(monster).get("Min Health"), monster_index.get("Verdant Forest").get(monster).get("Max Health"))
        monster_accuracy = monster_index.get("Verdant Forest").get(monster).get("Accuracy")
        monster_min_damage = monster_index.get("Verdant Forest").get(monster).get("Min Damage")
        monster_max_damage = monster_index.get("Verdant Forest").get(monster).get("Max Damage")
    
    elif world_map.tile_map.get((x,y)).get("Location") == "Shimmering Cave":
        monster_list = list(monster_index.get("Shimmering Cave"))
        monster = random.choice(monster_list)
        monster_max_hp = random.randint(monster_index.get("Shimmering Cave").get(monster).get("Min Health"), monster_index.get("Shimmering Cave").get(monster).get("Max Health"))
        monster_accuracy = monster_index.get("Shimmering Cave").get(monster).get("Accuracy")
        monster_min_damage = monster_index.get("Shimmering Cave").get(monster).get("Min Damage")
        monster_max_damage = monster_index.get("Shimmering Cave").get(monster).get("Max Damage")

    elif world_map.tile_map.get((x,y)).get("Location") == "The Desert":
        monster_list = list(monster_index.get("The Desert"))
        monster = random.choice(monster_list)
        monster_max_hp = random.randint(monster_index.get("The Desert").get(monster).get("Min Health"), monster_index.get("The Desert").get(monster).get("Max Health"))
        monster_accuracy = monster_index.get("The Desert").get(monster).get("Accuracy")
        monster_min_damage = monster_index.get("The Desert").get(monster).get("Min Damage")
        monster_max_damage = monster_index.get("The Desert").get(monster).get("Max Damage")

    elif world_map.tile_map.get((x,y)).get("Location") == "Howling Cliffs":
        monster_list = list(monster_index.get("Howling Cliffs"))
        monster = random.choice(monster_list)
        monster_max_hp = random.randint(monster_index.get("Howling Cliffs").get(monster).get("Min Health"), monster_index.get("Howling Cliffs").get(monster).get("Max Health"))
        monster_accuracy = monster_index.get("Howling Cliffs").get(monster).get("Accuracy")
        monster_min_damage = monster_index.get("Howling Cliffs").get(monster).get("Min Damage")
        monster_max_damage = monster_index.get("Howling Cliffs").get(monster).get("Max Damage")
        
    monster_hp = monster_max_hp
    turn = 1
    print("\n1. Enemy Encounter")

    # Main encounter loop
    while monster_hp > 0 and player_health > 0:
        print(f"\nTurn {turn} \n")

        # UI healthbar bariables
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
                    # Damage time 
                    monster_hp -= player_damage
                    
                elif decision == 2: # Healing Menu 
                    player_action_taken = BattleHealingMenu()
                else:
                    print("Please enter a valid number!\n")


        # Enemy Turn - provided it is still alive
        if monster_hp > 0:
            # Check for hit
            hit_roll = random.randint(1, 100)
            if hit_roll <= monster_accuracy:
                true_damage = random.randint(monster_min_damage, monster_max_damage)
                # Apply armour effects
                damage_taken = max(0, true_damage - player_damage_reduction)
                print(f"The {monster} attacks you. You take {damage_taken} damage.")
                player_health -= damage_taken
            else: 
                print(f"The {monster} attacks but misses!")
            
        turn += 1
    
    # Post-Battle calculations 

    if player_health <= 0:
        print(f"{player_name} was defeated...")
        EndingSequence("Bad Ending")
    elif monster_hp <= 0:
        # Grants gold to the player based on the difficulty of the monster encounter
        gold_gained = int((monster_max_hp * 0.5) + (monster_min_damage + monster_max_damage) / 2 + (monster_accuracy / 10))
        player_gold += gold_gained
        print(f"\n\nYou have slain the {monster}. You have gained {gold_gained} Gold. Your new total is {player_gold} Gold.\n\n———————————————————————————————————————————\n")
        world_map.tile_map.get((x,y)).update({"Battle Complete": True})
        ExplorationScreen(x,y)

def BossBattle():
    global player_max_health
    global player_health
    global player_name
    
    monster_list = list(monster_index.get("The Peak"))
    monster = random.choice(monster_list)
    monster_max_hp = random.randint(monster_index.get("The Peak").get(monster).get("Min Health"), monster_index.get("The Peak").get(monster).get("Max Health"))
    monster_accuracy = monster_index.get("The Peak").get(monster).get("Accuracy")
    monster_min_damage = monster_index.get("The Peak").get(monster).get("Min Damage")
    monster_max_damage = monster_index.get("The Peak").get(monster).get("Max Damage")

    player_damage = weapon_damage_index[equipped_weapon]
    player_damage_reduction = armour_reduction_index[equipped_armour]

    monster_hp = monster_max_hp
    turn = 1
    print(f"\nBoss Encounter - {monster}")

    while monster_hp > 0 and player_health > 0:
        print(f"\nTurn {turn} \n")
        # UI healthbar variables
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
                    # Damage time 
                    monster_hp -= player_damage
                    
                elif decision == 2: # Healing Menu 
                    player_action_taken = BattleHealingMenu()
                else:
                    print("Please enter a valid number!\n")

            # Enemy Turn - provided it is still alive
            if monster_hp > 0:
                # Check for hit
                hit_roll = random.randint(1, 100)
                if hit_roll <= monster_accuracy:
                    true_damage = random.randint(monster_min_damage, monster_max_damage)
                    # Apply armour effects
                    damage_taken = max(0, true_damage - player_damage_reduction)
                    print(f"The {monster} attacks you. You take {damage_taken} damage.")
                    player_health -= damage_taken
                # Otherwise, do not do damage to the player
                else: 
                    print(f"The {monster} attacks but misses!")
            # Increase turn number - this could easily be used for something, but it is just used for the turn display here
            turn += 1
    
    # Post-Battle calculations 
    if player_health <= 0:
        print(f"{player_name} was defeated...")
        EndingSequence("Bad Boss Ending")
    elif monster_hp <= 0:
        print(f"The {monster} has been slain!")
        EndingSequence("Good Ending")

# Function used for unlocking the two locked tiles present in the game
def UnlockGate(x,y):
    # Checks through the key items to see if the player can unlock the door
    for key_item in key_items_inventory:
        if key_item == world_map.tile_map.get((x,y)).get("Unlock Item") and key_items_inventory.get(key_item) > 0:
            print(f"\nGate unlocked! The {key_item} has been removed from your inventory.\n\n———————————————————————————————————————————\n")
            world_map.tile_map.get((x,y)).update({"Unlocked": True})
            key_items_inventory[key_item] -= 1
    # If the door's still not unlocked after going through all of the key items present in the inventory, end the function with a message communicating this to the player.
    if world_map.tile_map.get((x,y)).get("Unlocked") == False:
        print("\nYou do not have the required item to unlock this gate!\n\n———————————————————————————————————————————\n")
    ExplorationScreen(x,y)

# THIS is the main menu of the game, which every function stems from. 
def ExplorationScreen(x,y):
    decision = 0
    player_action_taken = False
    while player_action_taken == False:
        try:
            # Displays slightly different menus based on tile type - option 1 can either be 'No Option Available', 'Shop', 'Battle', or 'Interact'
            if world_map.tile_map.get((x,y)).get("Type") == "Plain":
                print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. No Option Available\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            # Battle tile display (depending on whether said battle tile is already completed) - Displays 'Battle' or 'Battle (Completed)'
            elif world_map.tile_map.get((x,y)).get("Type") == "Battle":
                if world_map.tile_map.get((x,y)).get("Battle Complete") == True:
                    print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {world_map.tile_map.get((x,y)).get("Type")} (Completed)\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
                else:
                    print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {world_map.tile_map.get((x,y)).get("Type")}\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            # Battle tile display (depending on whether said gate tile is open) - Displays 'Unlock Gate' or 'No Option Available (Gate Unlocked)'
            elif world_map.tile_map.get((x,y)).get("Type") == "Gate":
                if world_map.tile_map.get((x,y)).get("Unlocked") == False:
                    print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. Unlock Gate\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
                else:
                    print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. No Option Available (Gate Unlocked)\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            # Otherwise, just display the name of the tile
            else:
                print(f"\n{player_name} {player_health}/{player_max_health}HP {player_gold} Gold [X:{x}, Y:{y}] - {world_map.tile_map.get((x,y)).get("Name")}, {world_map.tile_map.get((x,y)).get("Location")}\n\n“{world_map.tile_map.get((x,y)).get("Description")}”\n\nWhat would you like to do?\n\n    1. {world_map.tile_map.get((x,y)).get("Type")}\n    2. Movement\n    3. Bag\n\n———————————————————————————————————————————\n")
            decision = int(input())
        # If the player enters a non-integer, handle the ValueError
        except ValueError:
            print("\nPlease enter a valid number!\n")
        else:
            if decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Gate": # Gate Unlock
                if world_map.tile_map.get((x,y)).get("Unlocked") == False:
                    player_action_taken = True
                    UnlockGate(x,y)
                else: 
                    print("\nPlease enter a valid number!\n")
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Interact": # Obtain item
                player_action_taken = True
                Interaction(x,y)
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Battle": 
                # Enemy encounter if the battle is not completed
                if world_map.tile_map.get((x,y)).get("Battle Complete") == True:
                    print("\nYou have already completed this battle!\n")
                if world_map.tile_map.get((x,y)).get("Battle Complete") == False:
                    player_action_taken = True
                    EnemyEncounter(x,y)
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Shop": # Shop Menu
                player_action_taken = True
                ShopMenu(x,y)
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Boss": # Boss battle (Game End)
                player_action_taken = True
                BossBattle()
            elif decision == 1 and world_map.tile_map.get((x,y)).get("Type") == "Plain": # No input on plain tiles
                print("\nPlease enter a valid number!\n")
            elif decision == 2: # Movement Menu
                player_action_taken = True
                MovementMenu(x,y)
            elif decision == 3: # Bag Menu
                player_action_taken = True
                BagMenu()
            # if the number is not 1, 2, or 3, handle the else
            else: 
                print("\nPlease enter a valid number!\n")





# it all runs from calling one beautiful function :3
StartSequence()

