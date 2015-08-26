Theseus and the Minotaur
=========================

About:
	This is a maze puzzle game in which the player tries to get 
Theseus (represented by *) to the end of the maze before the 
Minotaur (represented by #) is able to get to him. 
The challenge of the game comes with the fact the the Minotaur can 
move 2 spaces for every one of Theseus's. 
The advantage of the Minotaur forces the player to intellengently navigate Theseus in a way that traps him.

How to use:
	This program must be run from the terminal or the command prompt 
depending on whether you are using Windows, Linux, or OS X.

Linux: 
If you do not already have python installed do that first. 
Then simply navigate to the directory that you fork this repo to, 
and run ./gameplay.py to start the game. 

OSX:
Open Terminal and navigate to where you saved this directory. Run the command
"python gameplay.py" to start the game.

Windows:
In order to play on windows you must download python and add the game to your 
PATH variable.
In Windows 7 go to Control Panel > System and Security > System >
Advanced System Settings (on left panel) > Enironmental Variables.
Double click "path" under variables at the top and add C://Python33;
or whichever python version is listed in C:// (ie Python26).
Add a semicolon to the to the end of the entry before if there is not already
one there. Click "OK". Now run "cmd" from the windows command prompt, navigate
to the directory where the game is and type "python gameplay.py". 

Unix Philosophy:
	When building this project we tried to incorporate some Unix 
philosophy into the design. We attempted to use modular programming 
and keep a thin layer between the interface and the data manipulation 
in the background. The methods that print out the information are completely 
seperate from the methods that determine what to print next. We also 
implemented already written code for allowing the user to input unbuffered 
characters so that he or she wouldn't have to press enter everytime he or 
she wanted to move. This goes along with the open source, code distribution 
mentality that Unix relies on for its vitality. 
