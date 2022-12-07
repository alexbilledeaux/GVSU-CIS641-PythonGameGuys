# Overview

This document holds all the functional and non-functional requirements for our basic roguelike game, divided into categories and subcategories. These will be used to ensure that our game has everything working that it needs to.

# Functional Requirements

1. Game Menu
   1. The main menu shall display options to start a new game, to load a saved game and to quit.
   2. The game program shall exit when the user selects the quit option.
   3. The game shall allow the user to select one player class from {ranger, warrior, mage} when the user selects the “New game” option.
   4. A new game run shall start when the user selects a player class.
   5. The game shall allow the user to go back to the main menu from the player class selection menu.
  
2. Level Generation
   1. The level generator shall add at least 5 + n enemies per level, where n is the depth.
   2. The level generator shall generate a level where the exit is reachable.
   3. The level generator shall add at least 3 items per level.
   4. The enemy stats shall grow as the depth increases.
   5. The items and enemies added to the map shall grow better as the depth grows.
   6. The level generator shall have two different map creation algorithms.
   
3. Gameplay
   1. The game shall remove an enemy's icon from the map when the enemy's health reaches 0.
   2. The player shall attack an enemy by attempting to move onto the enemy's tile.
   4. The game shall prevent the player from moving into a tile that contains a wall.
   5. Enemies shall attempt to defeat the player by attacking them.
   6. The game shall end if the player's health reaches 0.
   7. An entity's health shall decrease by the attacker’s power minus the defender's defense when it is attacked.

4. Items
   1. The player shall only be able to equip one set of armor at a time.
   2. The player shall only be able to equip one weapon at a time.
   3. The game shall display a message when the player successfully equips a piece of equipment.
   4. The game shall display a message when the player successfully unequips a piece of equipment.
   5. The player shall be able to display the contents of his/her inventory.
   6. The game shall prevent the player from using a healing consumable when they are at maximum hitpoints.

5. Display and UI
   1. Once a game has started, the UI shall display an event log which shows the 5 most recent ones.
   2. The player's HP bar shall remain visible.
   3. The UI should display the current dungeon level.
   4. The game shall display tiles of the map as they are seen by the player.
   5. The game shall show entities on the map while they are in the player's field of view.
   6. The game shall hide entities on the map while they are not in the player's field of view.

# Non-Functional Requirements

1. Performance Requirements
   1. The level generator shall take no more than 10 seconds to create a new level.
   2. Navigating between menu screens shall not take more than 1 second.
   3. The game shall respond to player input within 0.5 seconds.
   4. A saved game file shall not exceed 2mb.
   5. A saved game shall load in no more than 1 second.
   6. The game executable shall not be larger than 300kb.
   7. The game shall not use more than 100 MB of RAM when it runs.

2. Compatibility Requirements
   1. The game shall be playable on Ubuntu 20.04.
   2. The game shall be playable on Windows 10 Home.
   3. The game shall be playable on MacOS Monterey 12.5.1.
   4. New standalone executables of the game shall be generated automatically after changes to the Github repository.
   5. The source code of the game shall be compilable using Python 3.7 or higher.

3. Security Requirements
   1. The game shall not store any information about the user.
   2. The game shall not request any administrator privilege to run.
   3. The game executable shall not modify any files except for savegame.sav.
   4. The game executable shall not modify any files outside of the folder where it is located.
   5. Users shall not be required to set up an account or enter user credentials to download the game executable.

4. Operational Requirements
   1. The game shall be playable using a keyboard.
   2. The game shall shall support the use of a mouse to select ranged targets on the game map.
   3. The game shall run as a standalone program.
   4. The game window shall be resizable and its contents shall scale accordingly.
   5. The game shall be packaged as a standalone executable.

5. Cultural and Political Requirements
   1. The menu options and messages shall be displayed in English.
   2. The entity class shall be identifiable by alphanumerics rather than color.
   3. The game source code shall be free to modify and redistribute according under the MIT License.
   4. The game shall be playable by users who are at least 12 years old.
   5. The game shall not include any political/religious reference either in text or visually.
