import simplegui
import random
import math

#global values
secret_number = None
guess_number = None
range = 100 #default range
guesses = 7 #default no. of guess

def new_game():
    global secret_number, range, guesses
    if range == 100:
        guesses = 7
    else:
        guesses = 10
    secret_number = random.randrange(0, range)
    print "\n"
    print "NEW NUMBER: Range is from 0 to", range
    print "Guesses left: ", guesses

#event handlers for control panel
def range100():
    global range, guesses
    range = 100
    guesses = 7
    new_game()

def range1000():
    global range, guesses
    range = 1000
    guesses = 10
    new_game()
    
def input_guess(guess):
    global secret_number, guesses
    guess_number = int(guess)
    guesses -= 1
    print "\n"
    print "Your Guess: ", guess_number
    print "Remaining Guess: ", guesses
    
    if secret_number == guess_number:
        print "You are Correct! The Number is ", secret_number
        new_game()
    else:
        if(secret_number>guess_number):
            print "Higher"
        elif(secret_number < guess_number):
            print "Lower!"
    if guesses <= 0:
        print "No more guesses! The correct number is ", secret_number
        new_game()

    
#create frame
frame = simplegui.create_frame('Number Game', 200, 200)

#Add buttons
frame.add_button('Range: 0 - 100', range100, 200)
frame.add_button('Range: 0 - 1000', range1000, 200)  
frame.add_input("What's your number?", input_guess, 200)

# call new_game 
frame.start()
new_game()
