# Overview

This document holds all the functional and non-functional requirements for our basic roguelike game, divided into categories and subcategories. These will be used to ensure that our game has everything working that it needs to.

# Functional Requirements

1.  Game Menu
    1. The main menu shall display options to both start a new game and to quit.
    2. The game program shall exit when the user selects the quit option.
    3. The game shall allow the user to select one player class of … when the user selects the “New game” option.
    4. A new game run shall start when the user selects a player class.
  
2. Level Generation
   1. The level generator shall add at least 5 + n enemies per level, where n is the depth.
   2. The level generator shall generate a level where the exit is reachable.
   3. The level generator shall add at least 3 items per level.
   4. The enemy stats shall grow as the depth increases.
   
3. Combat
   1. The game shall remove an enemy's icon from the map when the enemy's health reaches 0.
   2. The player shall attack an enemy by attempting to move onto the enemy's tile.
   3. The game shall prevent the player from using a healing consumable when they are at maximum hitpoints.
   4. The game shall prevent the player from moving into a tile that contains a wall.
   5. Enemies shall attempt to defeat the player by attacking them.
   6. The game shall end if the player's health reaches 0.
   7. An entity's health shall decrease by the attacker’s power minus the defender's defense when it is attacked.


# Non-Functional Requirements

1. Performance Requirements
    1. The level generator shall take no more than 10 seconds to create a new level.
    2. Navigating between menu screens shall not take more than 1 second.
    3. Each level shall be completable within 5 minutes.
    4. One full run shall take no more than 30 minutes.
    5. The player character shall have a maximum number of hitpoints that cannot be exceeded.

2. Security Requirements
    1. The game shall not store any information about the user.

3. Operational Requirements
    1. The game shall be playable on Windows 10 Home and MacOS Monterey 12.5.1.
    2. The game shall be playable using a keyboard.
    3. The game shall run as a standalone program.

4. Cultural and Political Requirements
    1. The menu options shall be displayed in English.
