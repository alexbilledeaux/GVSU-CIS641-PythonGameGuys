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
   1. The level generator shall have two different map creation algorithms - cave and dungeon.
   2. The level generator shall attempt to place between 0 and 1 enemies per room in the dungeon floor generator at depth level 1 to 3.
   3. The level generator shall attempt to place between 0 and 2 enemies per room in the dungeon floor generator at depth level 4 and 5.
   4. The level generator shall attempt to place between 0 and 3 enemies per room in the dungeon floor generator at depth level 6 and higher.
   5. The level generator shall attempt to place between 5 and 20 enemies per floor in the cave floor generator at depth level 2 and 3.
   6. The level generator shall attempt to place between 10 and 25 enemies per floor in the cave floor generator at depth level 4 and 5.
   7. The level generator shall attempt to place between 15 and 35 enemies per floor in the cave floor generator at depth level 6 and higher.
   8. The level generator shall generate a level where the exit is reachable.
   9. The level generator shall attempt to place between 0 and 1 items per room in the dungeon floor generator at depth level 1 to 3.
   10. The level generator shall attempt to place between 0 and 2 items per room in the dungeon floor generator at depth level 4 and 5.
   11. The level generator shall attempt to place between 0 and 3 items per room in the dungeon floor generator at depth level 6 and higher.
   12. The level generator shall attempt to place between 5 and 15 items per floor in the cave floor generator at depth level 2 and 3.
   13. The level generator shall attempt to place between 10 and 25 items per room in the dungeon floor generator at depth level 4 and 5.
   14. The level generator shall attempt to place between 15 and 30 items per room in the dungeon floor generator at depth level 6 and higher.
   15. The items and enemies added to the map shall grow better as the depth grows.
   
3. Gameplay
   1. The game shall replace an enemy's icon from the map with a red '%' when the enemy's health reaches 0.
   2. The player shall attack an enemy by attempting to move onto the enemy's tile.
   4. The game shall prevent the player from moving into a tile that contains a wall.
   5. Enemies shall attempt to defeat the player by attacking them.
   6. The game shall end if the player's health reaches 0.
   7. An entity's health shall decrease by the attacker’s power minus the defender's defense when it is attacked.
   8. Each attack shall do a minimum of one damage, regardless of power and defense.

4. Items
   1. The player shall only be able to equip one set of armor at a time.
   2. The player shall only be able to equip one weapon at a time.
   3. The game shall display a message when the player successfully equips a piece of equipment.
   4. The game shall display a message when the player successfully unequips a piece of equipment.
   5. The player shall be able to display the contents of their inventory.
   6. The game shall prevent the player from using a healing consumable when they are at maximum hitpoints.

5. Display and UI
   1. Once a game has started, the UI shall display an event log, 5 lines high, which shows the most recent messages.
   2. The player's HP bar shall remain visible.
   3. The UI shall display the current dungeon level.
   4. The game shall display tiles of the map as they are seen by the player.
   5. The game shall show entities on the map while they are in the player's field of view.
   6. The game shall hide entities on the map while they are not in the player's field of view.

# Non-Functional Requirements

1. Performance Requirements
   1. The level generator shall take no more than 2 seconds to create a new level.
   2. Navigating between menu screens shall not take more than 1 second.
   3. The game shall respond to player input within 0.5 seconds.
   4. A saved game file shall not exceed 100KB.
   5. A saved game shall load in no more than 1 second.
   6. The game executable shall not be larger than 10MB.
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
   3. The game executable shall not require any installation.
   4. The game window shall be resizable and its contents shall scale accordingly.
   5. The game shall be packaged as a standalone executable.

5. Cultural and Political Requirements
   1. The menu options and messages shall be displayed in English.
   2. The entity types {eg. scroll, arrow} shall be identifiable by alphanumerics rather than color.
   3. The game source code shall be free to modify and redistribute under the GNU General Public License V3.0.
   4. The game shall be playable by users who are at least 12 years old.
   5. The game shall not include any political/religious reference either visually or in text.
