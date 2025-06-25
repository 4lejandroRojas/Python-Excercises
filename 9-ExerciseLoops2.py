# Create a guess game with the names of the colors.
# At each round pick a random color from a list and let the user try to guess it.
# When he does it, ask if he wants to play again. Keep playing until the user types no

import random
colors = ["orange", "red", "blue"]

while(True):
    colorToGuess = input("Introduce the color to guess: ").lower()
    randomColor = colors[random.randint(0, len(colors)-1)]

    while (True):
        if(colorToGuess == randomColor):
            print("You got it")
            break
        else:
            colorToGuess = input("No, try it again: ")
    
    answerContinueToPlay = input("You got it. Want to continue playing? (Write 'no', to cancel): ").lower()
    if(answerContinueToPlay == "no"): break
