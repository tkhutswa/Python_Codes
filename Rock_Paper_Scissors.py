import random
from random import randint

print("""
    The Official Rock Paper Scissors Python Game
    ____________________________________________
    """)

print("""
      Please choose your option:
      
      (Rock, Paper or Scissors)
      
      """)

rock = """
            ,--.--._
        ------" _, \___)
                / _/____)
                \//(____)
        ------\     (__)
            `-----"

"""

paper = """
        
               _  / |
              / \ | | /-
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
                |     |
"""


scissors = """
                _    _ - - - 
            (_).  ,/'
            _  ::
            (_)'  `\.
                    `\.- - -
"""

choice = [scissors + "Computer Choice: Scissors", paper + "Computer Choice: Paper", rock + "Computer Choice: Rock"]

option1 = random.choice(choice)

option2 = random.choice(choice)

user = input("Your Choose:")


if user == "scissors":
    print(scissors + """    User Choice: Scissors   """)
    print(option1)
    
    print(f"""
          User Wins the Game!!
          """)
    
if user == "rock":
    print(rock + """    User Choice: Rock     """)
    print(option1)
    
if user == "paper":
    print(paper + """    User Choice: Paper    """)
    print(option1)
    
# if user == "paper" and option1 == paper: 
#     print(f"""
#           Its a Tie!!
#           """)

 
if option1 == choice[0]:
    print()
    pass





