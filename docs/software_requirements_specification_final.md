# Overview

This document is the final deliverable for the Python Game Guys 641 Semester Project. Included are final software requirements, change control information, traceability between artifacts and requirements, and links to all the artifacts generated for the project.

# Software Requirements

This section holds all of our software requirements, starting with functional, then non-functional. 

## Functional Requirements

### Game Menu

| ID | Requirement |
| :-------------: | :----------: |
| FR1 | The main menu shall display options to start a new game, to load a saved game and to quit. |
| FR2 | The game program shall exit when the user selects the quit option. |
| FR3 | The game shall allow the user to select one player class from {ranger, warrior, mage} when the user selects the “New game” option. |
| FR4 | A new game run shall start when the user selects a player class. |
| FR5 | The game shall allow the user to go back to the main menu from the player class selection menu. |
  
### Level Generation

| ID | Requirement |
| :-------------: | :----------: |
| FR6 | The level generator shall have two different map creation algorithms - cave and dungeon. |
| FR7 | The level generator shall attempt to place between 0 and 1 enemies per room in the dungeon floor generator at depth level 1 to 3. |
| FR8 | The level generator shall attempt to place between 0 and 2 enemies per room in the dungeon floor generator at depth level 4 and 5. |
| FR9 | The level generator shall attempt to place between 0 and 3 enemies per room in the dungeon floor generator at depth level 6 and higher. |
| FR10 | The level generator shall attempt to place between 5 and 20 enemies per floor in the cave floor generator at depth level 2 and 3. |
| FR11 | The level generator shall attempt to place between 10 and 25 enemies per floor in the cave floor generator at depth level 4 and 5. |
| FR12 | The level generator shall attempt to place between 15 and 35 enemies per floor in the cave floor generator at depth level 6 and higher. |
| FR13 | The level generator shall generate a level where the exit is reachable. |
| FR14 | The level generator shall attempt to place between 0 and 1 items per room in the dungeon floor generator at depth level 1 to 3. |
| FR15 | The level generator shall attempt to place between 0 and 2 items per room in the dungeon floor generator at depth level 4 and 5. |
| FR16 | The level generator shall attempt to place between 0 and 3 items per room in the dungeon floor generator at depth level 6 and higher. |
| FR17 | The level generator shall attempt to place between 5 and 15 items per floor in the cave floor generator at depth level 2 and 3. |
| FR18 | The level generator shall attempt to place between 10 and 25 items per room in the dungeon floor generator at depth level 4 and 5. |
| FR19 | The level generator shall attempt to place between 15 and 30 items per room in the dungeon floor generator at depth level 6 and higher. |
| FR20 | The items and enemies added to the map shall grow better as the depth grows. |
   
### Gameplay

| ID | Requirement |
| :-------------: | :----------: |
| FR21 | The game shall replace an enemy's icon from the map with a red '%' when the enemy's health reaches 0. |
| FR22 | The player shall attack an enemy by attempting to move onto the enemy's tile. |
| FR23 | The game shall prevent the player from moving into a tile that contains a wall. |
| FR24 | Enemies shall attempt to defeat the player by attacking them. |
| FR25 | The game shall end if the player's health reaches 0. |
| FR26 | An entity's health shall decrease by the attacker’s power minus the defender's defense when it is attacked. |
| FR27 | Each attack shall do a minimum of one damage, regardless of power and defense. |

### Items
| ID | Requirement |
| :-------------: | :----------: |
| FR28 | The player shall only be able to equip one set of armor at a time. |
| FR29 | The player shall only be able to equip one weapon at a time. |
| FR30 | The game shall display a message when the player successfully equips a piece of equipment. |
| FR31 | The game shall display a message when the player successfully unequips a piece of equipment. |
| FR32 | The player shall be able to display the contents of their inventory. |
| FR33 | The game shall prevent the player from using a healing consumable when they are at maximum hitpoints. |

### Display and UI
| ID | Requirement |
| :-------------: | :----------: |
| FR34 | Once a game has started, the UI shall display an event log, 5 lines high, which shows the most recent messages. |
| FR35 | The player's HP bar shall remain visible. |
| FR36 | The UI shall display the current dungeon level. |
| FR37 | The game shall display tiles of the map as they are seen by the player. |
| FR38 | The game shall show entities on the map while they are in the player's field of view. |
| FR39 | The game shall hide entities on the map while they are not in the player's field of view. |

## Non-Functional Requirements

### Performance Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | The level generator shall take no more than 2 seconds to create a new level. |
| NFR2 | Navigating between menu screens shall not take more than 1 second. |
| NFR3 | The game shall respond to player input within 0.5 seconds. |
| NFR4 | A saved game file shall not exceed 100KB. |
| NFR5 | A saved game shall load in no more than 1 second. |
| NFR6 | The game executable shall not be larger than 10MB. |
| NFR7 | The game shall not use more than 100 MB of RAM when it runs. |

### Compatibility Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR8 | The game shall be playable on Ubuntu 20.04. |
| NFR9 | The game shall be playable on Windows 10 Home. |
| NFR10 | The game shall be playable on MacOS Monterey 12.5.1. |
| NFR11 | New standalone executables of the game shall be generated automatically after changes to the Github repository. |
| NFR12 | The source code of the game shall be compilable using Python 3.7 or higher. |

### Security Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR13 | The game shall not store any information about the user. |
| NFR14 | The game shall not request any administrator privilege to run. |
| NFR15 | The game executable shall not modify any files except for savegame.sav. |
| NFR16 | The game executable shall not modify any files outside of the folder where it is located. |
| NFR17 | Users shall not be required to set up an account or enter user credentials to download the game executable. |

### Operational Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR18 | The game shall be playable using a keyboard. |
| NFR19 | The game shall shall support the use of a mouse to select ranged targets on the game map. |
| NFR20 | The game executable shall not require any installation. |
| NFR21 | The game window shall be resizable and its contents shall scale accordingly. |
| NFR22 | The game shall be packaged as a standalone executable. |

### Cultural and Political Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR23 | The menu options and messages shall be displayed in English. |
| NFR24 | The entity types {eg. scroll, arrow} shall be identifiable by alphanumerics rather than color. |
| NFR25 | The game source code shall be free to modify and redistribute under the GNU General Public License V3.0. |
| NFR26 | The game shall contain no adult themes. |
| NFR27 | The game shall not include any political/religious reference either visually or in text. |


# Change Control

This game is easy to implement due to it being packaged for Windows, MacOS, and Linux. There are no extra installations. Training will be through a text document explaining what the controls and icons mean. Features include randomly generated levels, so that the layout and item/enemy placement will be different each time, adding to the longevity of the game. In addition, there are three different classes to play and master - the ranger, whose mastery of ranged combat will keep you safe, the warrior, whose strength will leave your foes stumbling in their tracks, and the mage, whose ability to potentially reuse scrolls means you will be a powerhouse if you can survive the early levels.

We will use a ticket-based system for reporting and resolving bugs, using Github’s Issues page. The page has been enabled in the repository’s settings and a subheading in the games ReadMe will have the following text, instructing users on how to report bugs for the game.

# Traceability Links

In this section, we have listed all artifacts and the functional/nonfunctional requirements that they fulfill.

## Use Case Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |


## Class Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |


## Activity Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |


# Software Artifacts

This section contains all the links to the actual artifacts in the github repository.

* [Attack Entity and Use Item Activity Diagrams](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/AttackEntity_UseItem_ActivityDiagrams.pdf)
* [Attack Entity Use Case](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/Attack_MethodSpecification.pdf)
* [Enemy Class and Object Diagram](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/Enemy%20Class%20and%20Object%20Diagram.pdf)
* [Class Diagram](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/Combined_Team_Class_Diagram-Page-1.pdf)
* [Actor/Inventory/Item/Consumable/Equippable Object Diagrams and Descriptions](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/ClassDescription_ObjectDiagram_Actor_Inventory_Item_Consumable_Equippable.pdf)
* [Engine/GameMap/GameWorld Object Diagrams and Descriptions](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/ClassDescription_ObjectDiagram_Engine_GameMap_GameWorld.pdf)
* [Message/MessageLog/Fighter/Entity Object Diagrams and Descriptions](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/ClassDescription_ObjectDiagram_Message_MessageLog_Fighter_Entity.pdf)
* [Fighter and Actor Database Table](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/Fighter_Actor_Database_Table.pdf)
* [Gameplay and Menu/Interface Use Case Diagrams](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/Gameplay_MenuInterface_UseCaseDiagram.pdf)
* [State Machine Diagram](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/State%20Machine%20Diagram.pdf)
* [Behavior Diagram](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/blob/master/artifacts/behavior%20diagram.pdf)
