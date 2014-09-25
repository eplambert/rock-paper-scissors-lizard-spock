# Eric Lambert
# September 24, 2014

# Rock-paper-scissors-lizard-Spock
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    This function takes in one of 5 names and returns its
    number equivalent
    """
    num = 0
    if name == 'rock':
        return num
    elif name == 'Spock':
        num = 1
        return num
    elif name == 'paper':
        num = 2
        return num
    elif name == 'lizard':
        num = 3
        return num
    elif name == 'scissors':
        num = 4
        return num
    else:
        print "An incorrect name has been entered"
    

def number_to_name(number):
    """
    This function takes in a number and converts the number
    to its corresponding name
    """
    if number == 0:
        name = 'rock'
        return name
    elif number == 1:
        name = 'Spock'
        return name
    elif number == 2:
        name = 'paper'
        return name
    elif number == 3:
        name = 'lizard'
        return name
    elif number == 4:
        name = 'scissors'
        return name
    else:
        print "An incorrect number has been entered"  

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player chooses ", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses ", comp_choice

    # compute difference of comp_number and player_number modulo five
    winner = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if winner > 2:
        print "Player wins!"
    elif winner < 3 and winner > 0:
        print "Computer wins!"
    else:
        print "Player and Computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
