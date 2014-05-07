			Theseus and the Minotaur
About:
	This is a maze puzzle game in which the player tries to get to Theseus (the question mark) to the end of the maze before the Minotaur (the dollar sign) is able to get to him. The challenge of the game comes with the fact the the Minotaur can move 2 spaces for every one of Theseus's one move. The advantage of the Minotaur forces the player to intellengently navigate Theseus in a way that traps him.

How to use:
	This program must be run from the terminal. Simply navigate to the directory that you fork this repo to, and run ./gameplay to start the game. Instructions on how to play are given within the game. 

Unix Philosophy:
	When building this project we tried to incorporate some Unix philosophy into the design. We attempted to use modular programming and keep a thin layer between the interface and the data manipulation in the background. The methods that print out the information are completely seperate from the methods that determine what to print next. We also implemented already written code for allowing the user to input unbuffered characters so that he or she wouldn't have to press enter everytime he or she wanted to move. This goes along with the open source, code distribution mentality that Unix relies on for its vitality. 
