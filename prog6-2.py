# Assignment 6
# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)


print("Welcome to your Virtual Addition Training Generator!")

from random import randint

def trainer_():
    first_ = randint(0, 100)
    second_ = randint(0, 100)
    return first_, second_

level = 1
points_ = 0

while level != 11:
    addend_1, addend_2 = trainer_()
    print("Addition practice", level ,"will now commence! You can do this!\nYour current points is", points_ )
    key_ = int(input(f"Calculate the following:\n {addend_1} plus {addend_2} is? "))
    answer_key = addend_1 + addend_2
    if answer_key == key_ :
        level += 1
        points_ += 1
    else:
        level += 1

def finish_ed():
    print("Overall points:", points_, " Thank you for working hard in today's addition training! \n See you again! ")
finish_ed()