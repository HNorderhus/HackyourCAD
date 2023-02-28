
# Checkers Board Game

# Description

This is the final project for the module Foundations of CAD with FreeCAD and Python at the Bauhaus University Weimar in the wintersemester 2022/23. 
A completely functional version of the classic boardgame Checkers has been implemented in FreeCAD using only the available Python libraries.
It has been worked on by Morris Florek, matr. nr. 124437, and Henrik Norderhus, 123917, both students of the master program Digital Engineering.

The idea was to find out, whether an open-source CAD program can be repurposed to function as a simplistic gaming platform. 
To fulfill this goal the focus was put on the programming aspect, leading to a modelling:programming ratio of 20:80. Besides this, the project should reflect the lessons learnt throughout the students master's program, especially the respective FreeCAD course, which is why high expectation regarding the code's extent was expected from the beginning.

# How-to 

* To play the Checkers game, first download the .FCStd file and the Python files from the src folder. 
* Open the .FCStd file and copy the Python scripts to your local Freecad's scripting folder, this should be a hidden Folder under User/AppData/Roaming/FreeCAD/Macro. 
* Copy the Python files into the folder, making sure that no other Python scripts with the same name exist that directory.
* In FreeCAD, open the Makros window and select the main.py script. Click edit, the Python script will open in a new tab. Make sure that under View -> Panels you have selected both Report View and Python Console.
* Now, click the Play button on top of the taskbar while in the main.py-tab.
* Switch to the checkers.FCStd-tab, the game is now running. The Report View will tell you about the necessary input in the Python console. 
* !! In the beginning you need to select whether you want to play against a human adversary or against the computer. If you select "2", the computer, then you will need to select the difficulty in the next step, as instructed in the Report View. Make sure to manually delete the 2 from the console since no need input prompt will be generated and make sure to spell the difficulty setting correctly. !! 
* 



# Minimax algorithm

# Reflection

### TODO

##### Visuals

- [x] Create board
- [x] Create tokens
- [ ] Decide on camera angles
- [ ] Place lighting
- [ ] Background and general presentation in FreeCAD

##### Coding

- [x] Make board unselectable
- [x] Make only tokens selectable
- [ ] Move tokens with mouse click
- [ ] Highlight fields the token can move to
- [ ] Rotate camera via macro or turnbased
- [ ] Implement game rules (turn token into queen, remove other pieces ...)

##### Extras

- [ ] Animate the token's movement and removal
- [ ] Animate the preparation of the board for the next game
- [ ] Have a GUI displaying the score or option to restart the game
- [ ] Implement computer's logic
