# GVSU-CIS641-PythonGameGuys

We are creating a single-player roguelike game. In it, the player will explore procedularly generated maps, seeking the exit while defeating enemies and acquiring items to increase their survivability. When the player reaches the exit, a new map will be generated, featuring stronger enemies and items based on how many maps they have completed in their current run. There will be three classes to choose from, multiple enemy types to defeat, and the game will continue until the player is defeated.

The roguelike tutorial we used can be found [here](http://rogueliketutorials.com/tutorials/tcod/v2/)

The cellular automata tutorial we used can be found [here](https://gamedevelopment.tutsplus.com/tutorials/generate-random-cave-levels-using-cellular-automata--gamedev-9664)

## Team Members and Roles

* [Alex Billedeaux](https://github.com/alexbilledeaux/CIS641-HW2-Billedeaux)
* [Dan Dietsche](https://github.com/dannnnnnnnnn10/CIS641-HW2-Dietsche)
* [Luis Gomez](https://github.com/lgomezm/CIS641-HW2-Gomez)

## Prerequisites
This game has no prerequisites to run, if you intend to play it with one of our packaged executables. If you're interested in running the source code, you'll need to download the contents of this Github repository. Scroll to the top of the page, select '<> Code' in the menu, and select Download ZIP from the dropdown that appears.

Once the source code is present on your computer, you'll need to install Python 3.7 or higher to compile the source code and run the game. Head over to the [Python downloads](https://www.python.org/downloads/) page to get a version of the software that is appropriate for your computer. After you've installed python, open your Command Prompt or Terminal and navigate to the GVSU-CIS641-PythonGameGuys folder you downloaded. The game source code is located in the /src subdirectory. From the /src directory, run the following two commands.  

pip install -r requirements.txt  
python3 main.py


## Run Instructions
To run the game, go to our [automated builds page](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/actions/workflows/python-package.yml), choose the most recent build, and scroll down until you see the heading 'Artifacts'. There is a ZIP file titled 'automated-builds'. The file contains a Windows, Mac, and Linux builds of the game. Download the ZIP, uncompress the contents, and select the executable that is right for your computer. You're ready to play!

## Found a Bug?
Thanks for contributing to our roguelike! Visit our [issues page](https://github.com/alexbilledeaux/GVSU-CIS641-PythonGameGuys/issues) and see if your issue has already been reported for the repo. If you don’t see anything similar, select the New Issue button to report your bug. Our team is composed entirely of volunteers, so we can’t provide an immediate timeline on bug fixes. Thanks for your patience.

## How to Play
Our game is an infinite roguelike, which means that you'll be delving into a multi-level dungeon and trying to get as deep as possible before dying. Each time you die, you'll restart the game from the beginning without carrying over any items or experience from your previous run.

### The Classes
Our roguelike has three player classes to choose from. The first class is the Ranger, who starts each run with a shortbow, light armor, and ten arrows. They specialize in the bow and have the ability to recover arrows from fallen enemies. The second class is the Warrior, who starts each run with heavy armor and a dagger. They specialize in melee combat and their strikes occassionally cause enemies to become dazed. Finally, you can play as the Mage. The Mage starts each run with several magic scrolls and has the ability to occasionally recover magic scrolls after use.

### The Keyboard Controls
| Key | Control |
| :----: | :----: |
| Up Arrow | Move Up |
| Left Arrow | Move Left |
| Right Arrow | Move Right |
| Down Arrow | Move Down |
| Home | Move Up + Left |
| Pg Up | Move Up + Right |
| End | Move Down + Left |
| Pg Down | Move Down + Right |
| . | Wait |
| i | Open Inventory |
| d | Drop Item from Inventory |
| g | Pick Up |
| c | View Character |
| v | Message History |
| ctrl+. | Use Stairs |
| esc | Exit Menu or Exit Program |
