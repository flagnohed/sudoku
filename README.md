# sudoku
Solves sudoku problems, atleast some of them...

Due to limited knowledge in sudoku, only easy and medium sudoku problems can be solved. It currently doesn't have a GUI, so it's done in terminal with user input.

TODO: 

* Implement other sudoku techniques to solve harder problems
* Implement GUI

Techniques implemented (number removal):
* Sole candidate
* Unique candidate

Techniques to be implemented (candidate removal):
* Block/block interaction
* Naked subset
* Hidden subset
* X-wing
* Swordfish

How to use:

Run the file main.py. 
In the terminal, input each row from the sudoku problem as a string, e.g., "123456789". 
Unknown cells are denoted with 0. The program outputs a nested list where every sublist represents a row in the sudoku board.
