Team name: Python Game Guys

Team members: Alex Billedeaux, Luis Gomez, Dan Dietsche

# Introduction

We are creating a single-player roguelike game. In it, the player will explore procedularly generated maps, seeking the exit while defeating enemies and acquiring items to increase their survivability. When the player reaches the exit, a new map will be generated, featuring stronger enemies and items based on how many maps they have completed in their current run.

At the beginning of each run, the player will choose between three classes, which modify player attributes such as health, damage, and FOV, to encourage differing playstyles. There will be three enemy types, with varying behaviors and attributes, with the stronger types beginning to show up on deeper maps. The game will continue until the player character is defeated, and the total number of completed maps in the run will be displayed on the screen. 

# Anticipated Technologies

Python 3.7+, TCOD package, VS Code IDE, and github

# Method/Approach

We will use [this tutorial](http://rogueliketutorials.com/tutorials/tcod/v2/) as a jumping off point, starting with implementing the features described in the guide. From there, we will expand on the project with additional enemy types, player classes, and items.

# Estimated Timeline

Total timeline will be a single semester, broken up into the following milestones, paraphrased from [the class page](https://gvsu-cis641.github.io/gvsu-cis641/term-projects/#project-responsibilities):
* Create Requirements Specification/CRC Cards (1 month)
* Create Functioning Prototype based off of tutorial (1 month)
* Expand on prototype to create final deliverable (1 month)

# Anticipated Problems

The team does not have much experience programming in python, using this as an opportunity to get familiar with the language. We are following the tutorial linked above as a way to mitigate this problem. Another risk that has been identified is that we are adding additional functionality not covered in the tutorial, such as player classes and additional enemy types, which may cause unforseen structural issues in how we organize the system. To mitigate this risk, we will strictly limit the number of classes/enemy types added to attempt to avoid scope creep. 
