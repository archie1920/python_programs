#craps roller
#demonstrates random number generation

import random

#generate random number 1 - 6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("\nYou rolled a",die1,"and a", die2, "for total of ",total)


