# Basic Structure for a Random Walk simulation
# Evan Sauers
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Set the ranges equal to the given integers
startRange = 100
endRange = 1001
stepRange = 10

# Give the ranges a distance
def main():
    printHeader()
    for n in range(startRange,endRange,stepRange):
        averageDistance = getRandomWalk(n)
        print("For {} steps, the average distance is: {}".format(n,averageDistance))

# Informing the user of the displacement
def printHeader():
    print("The displacement:")

# Giving the displacement results by adding or subtracting number of steps
def getRandomWalk(steps):
    step = 0
    for toss in range(steps):
        coin = random.randint(0,1)
        if coin == 1:
            step = step + 1
        else:
            step = step - 1
    return step

if __name__ == "__main__":
    main()