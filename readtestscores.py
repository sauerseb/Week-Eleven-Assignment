# Evan Sauers
# readtestscores.py
# Week Eleven Assignemnt
# Collaborated with Dr.Neumann and Rebekah Orth

# Import from the BowlingGame.py file
from BowlingGame import Game

# Read the File
newFile = open("testscores.txt", "r")
scoresList = []

# Bulk of the coding to analyze the file
for line in newFile:
    
    # Strip each line and split the numbers using a comma
    line = line.strip()
    scoresList = line.split (",")
    scoresList = [int(e) for e in scoresList]
    totalScore = scoresList.pop()
    
    # Note g is from the BowlingGame.py file
    g = Game()
    
    # Number of Pins
    for pins in scoresList:
        g.roll(pins)
    score = g.score()
    
    # Give the User the scores
    print ("Your score is {}, and the original given score is {}" .format(score, totalScore))
    if score == totalScore:
        print ("Correct! The scores are the same.")
    else:
        print ("Incorrect! The score is supposed to be", score)

# Close the file
newFile.close()

# From the findings, you can clearly see that the incorrect score total is from line 5