# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/


#Define the Game Paragraphs and Answers in this section
easy_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___2___ takes by
adding ___3___ separated by commas between the parentheses. ___1___s by default return ___4___ if you
don't specify the value to return. ___5___ can be standard data types such as string, number, dictionary,
tuple, and ___6___ or can be more complicated such as objects and lambda functions.'''
easy_answers = ['function', 'user', 'expressions', 'none', 'variables', 'lists']

medium_paragraph = '''Python Flow Contol and Loops:  In Python the ___1___ statement can be
used to control which code gets executed when.  The ___2___ loop performs the same task as
long as a condtion exists or is True.  [For example: ___2___ <condtion> :  then execute the
code following the loop that is indented.  The ___3___ loop can be used repeat the same task
a set number of times [For example: ___3___ num in range(10:):  then execute the code following
the loop that is indented].  The ___4___ statement is associated with a loop statement and is
executed when the loop has completed its iteration or is executed when a condition changes.
There is one way to stop the loop and that is with the use of the ___5___ statement.  When the
___2___ loop encounters this statement the program excexution is passed to the next line of code
outside of the loop.'''
medium_answers = ['if', 'while', 'for', 'else', 'break']

hard_paragraph = '''Structured Data can be in the form of strings and ___1___s.  A ___1___ can contain
characters, strings, numbers or other ___1___s.  ___2___ brackets contain all the elements and the
elements of a ___1___ and are separated by commas.  The List can be assigned a variable and the elements within
the list can be reference with an ___3___ number starting with number ___4___.  To add a new element
to the end of the list we can use the ___5___ method, which looks like this <list>.___5___ (<element>).
An operator that works on list the ___6___ and when used it will concatenate two list together.  another
operator that will work on lists is the ___7___.  The output is the number of elements contained within
the list.  Example ___7___(<list>).'''
hard_answers = ['list', 'square', 'index', 'zero', 'append', 'plus' 'len']



def start_game():
    '''This function builds the input for user game selection.  It will
    loop until one of three correct choices are entered by the user easy, medium or hard.
    As the output the function will return the game_level.'''
    print 'Please select a game difficutly by typing it in.'
    print 'Possible choices are easy, medium or hard?'
    game_level = (raw_input('? ')).lower()
    while game_level not in ['easy', 'medium', 'hard']:
        print
        print 'You have entered an incorrect game level, plese try again.'
        print 'Please select a game difficutly by typing it in.'
        print 'Possible choices are easy, medium or hard?'
        game_level = (raw_input('? ')).lower()
    print
    print 'You have chosen ' + game_level
    print
    print 'You will get 5 guesses per problem'
    print
    return game_level


def get_user_input(blank, num_max_attempts, answer, blank_number):
    '''This function prompts the user for their answer or guess and will convert it
    to all lower case to check against the real answer, but will display the users original
    input when we print out the paragraph.  The user may have entered in different capitalization
    than what the hard coded answer contained.  users_answer_or_guess will contain the users input.
    It will return False is user exceeded the maximum number of attempts. Input Variables 1) blank -
    which is the sting of the blank line and number that the user is entering in an answer for;
    2) num_max_attempts is the maximum number of attempts to an answer that the user can make;
    3) answer is the correct answer to the blank in quesiton. 4)blank_number is the interger
    value of the blank.'''
    num_wrong_guesses = 1

    #while num_wrong_guesses <= num_max_attempts:
    for index in range(num_max_attempts):
        print
        users_answer_or_guess = raw_input('What should be substituted in for ' + blank + '? ')
        users_answer_or_guess_lower_case = users_answer_or_guess.lower()
        if users_answer_or_guess_lower_case == answer:
            print
            print 'Good Job!!! You entered in the correct answer for blank ' + str(blank_number) + ' asnswer = ' + users_answer_or_guess
            print
            return users_answer_or_guess
        else:
            if num_wrong_guesses <= 4:
                print 'That isn\'t the correct answer!  Let\'s try again; you have ' + str((num_max_attempts - num_wrong_guesses)) + ' trys left!'
        num_wrong_guesses += 1
    return False

def select_difficulty(game_level):
    '''This funciton will take as input the game_level as previously selected by the
    user and return as outut the paragraph and list of answers corresponding to the
    game level, which is easy, medium or hard.'''
    if game_level == 'easy':
        paragraph = easy_paragraph
        answers = easy_answers
    elif game_level == 'medium':
        paragraph = medium_paragraph
        answers = medium_answers
    else:
        paragraph = hard_paragraph
        answers = hard_answers
    return paragraph, answers

def game_play(paragraph, answers):
#Define variables to be used in the rest of the code.
#For the user slected game level, loop thru each blank as defined in the paragraph.  The blank numbers (1,2,3,... etc)
#will correspond to the items as defined in the answer list.  We will also use a game over flag to indicate
#that the user has exceeded the maximum number of attempts to fill in the blank otherwise the loop
#will stop when we exceed the number of answers that are available from the list of answers.

    #Definition of constants
    num_max_attempts = 5    #maximum number of trys a user can have at guessing the correct answer for a blank
    blank_number = 1        #starts the numbering sequence of the blanks used in the paragraph
    game_over = False       #Flag to indicate if the user has exceeed the maximum number of attempts at guessing an answer
    answer_num = 0          #starts the counter for which answer from the predfined list of answers we are looking at

    #print the initial paragraph for the first go around
    print 'The current paragraph reads as such: \n'
    print paragraph

    while blank_number <=len(answers) and game_over == False:
        blank = '___' + str(blank_number) + '___'       #blank_number start counting at zeor
        answer = answers[answer_num]

        #Get user's input and return their original answer if correct or False if they exceed the max number of attempts
        user_response = get_user_input(blank, num_max_attempts, answer, blank_number)
        if user_response == False:
            print  '\n You have exceeded the maximum number of attempts.  To try again, please restart the game.'
            game_over = True
        else:
            paragraph = paragraph.replace(blank, user_response)
            print 'The current paragraph reads as such: \n'
            print paragraph
            if blank_number == len(answers):
                print '\n Congratulations!!! You have successfully completed the game by answering all the questions correctly!!!'
        blank_number += 1
        answer_num += 1

#START OF THE GAME CODE - MAIN BODY OF THE PROGRAM
game_level = start_game()

#retreive the paragraph and answers selected and used in the game
paragraph, answers = select_difficulty(game_level)

#call the funciotn to play the game
game_play(paragraph, answers)
