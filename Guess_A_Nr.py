#Generate a random number and track how many times did it take the user to get it right

import random
from random import randint
rand = randint(1, 3)

attempts =  0

user = int(input("Guess the Number! \n"))

while user:
    # print("You got it correct")
    if user == rand:
        print("You got it", rand, "after {} attempts".format(attempts))
        break

    else:
        print("try again")
        attempts += 1
        print("number of attempts: ",attempts)

        user = int(input("Guess the Number! \n"))
print(rand, user)

