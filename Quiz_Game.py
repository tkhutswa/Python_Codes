#quiz game, ask number of questions and if correct add 1 to their score board.
answers = [4,"capetown"]
score = 0

def verify():
    global score
    Q1 = int(input("How many Seasons do we have in a year? \n"))
    Q2 = str(input("What is the most attractive citities in South Africa: \n"))


        
    if Q1 in answers:
        score += 1
    elif Q2 in answers:
        score += 2
        print(score)
 
    else:
        print("You Lost")
        if score == 2:
            print("You won!")
        else:
            print("You Lost")
        

        print("Your score is: {}".format(score))

print("Welcome to the Quiz Game - Have fun!!")
verify()









