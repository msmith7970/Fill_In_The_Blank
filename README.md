# Project - Fill In The Blank Game


## Instructions - Download the program from GitHUb

Download and install this one python file from GitHUb to a PC that has Python
installed to the same directory.

    1) fill-in-the-blanks_project.py
    2) Answers.MD
    3) README.MD


## About the Game


### Game Basics

This game has three levels, 1) easy 2) medium and 3) hard.  


### Beginning the Game

Immediately after starting the program the user is prompted to select one of
the difficulty levels.  Once a level has been selected the game displays a
fill-in-the-blank and the user is prompted to fill in the first blank.  


### Game Play

When the player guesses correctly, the blank is replaced with the correct word
and the user is prompted for the next blank.

When a player guesses incorrectly, they are prompted to try again.

When a player guesses all the blanks correctly then the user is shown a
Successful message.


## About the Python Code

The Python Code used to create this game shows the use of programming concepts
to include:

    1) The use of Variables.
    2) The use of Functions with the use of a return statement.
    3) Appropriate data types are used consistently (strings for text, list for
      ordered data, nested lists).
    4) The use of branching techniques and loops.
    5) The use of decision statements using IF.
    6) The use of commenting code to explain what a particular piece of code is
    to accomplish.


# Initial Message

When the player selects a level they will see a response that tells which level
they have selected and a note that they will get 5 changes to guess correctly.
If the correct answer is not given in 5 tries the game will terminate and the
player will have to restart the game to try again.

```python
print 'You have chosen ' + game_level
print
print 'You will get 5 guesses per problem'
```


# Completion Message

When the player has answered all the blanks correctly they will get a
Congratulations message.

```Python
print 'Congratulations!!! You have successfully completed the \
       game by answering all the questions correctly!!!
```


## License

The content of this repository is licensed under MIT License.

Copyright (c) 2017 Mitchell Smith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
