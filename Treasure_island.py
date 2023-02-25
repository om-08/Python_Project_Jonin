print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

your_answer = input("There is a two way road were do you want to go left or right ? ")

if your_answer=="left":
    transport = input("You see a  river ahead and a boat is coming towards you but would u rather wait or start to swim to procced further either type 'wait' or 'swim ! ")
    if transport =="wait":
        print("After crossing  the river succesfully now you see a big door locked and u got three buttons ")
        buttons = input("The three buttons are red, blue and yellow to procceed in the quest choose one color button ! ")
        if buttons=="red":
            print("Burned By fire Game over !")
        elif buttons=="blue":
            print("Eaten By beasts Game Over.")
        elif buttons == "yellow":
            print("Winner Winner Chicken / Panner Dinner")
        else:
            print("You lost as you  choose the colour which was not in the option please choose accordingly in the next try ")
    else:
        print("Attacked by goblins u die  ! game over")

else:
    print("you fell into the hole and died ! game over")
    











    