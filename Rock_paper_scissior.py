rock = '''
    _______
---'   ____)                                               
      (_____)                                               
      (_____)                                           
      (____)                                     
---.__(___)                                       
'''

paper = '''
    _______
---'   ____)____                                               
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = input("What do you choose? type 0 for Scissors ✂, 1 for rock 🥌, 2 for paper 📃 ")
user_choice = int(user_input)                                   #user input can be taken using list as well
import random

computer_input = random.randint(0,2)
print(computer_input)
if computer_input == 0:
    print("Computer choose scissors" ,scissors)
elif computer_input == 1:
    print("Computer choose rock" ,rock)
elif computer_input ==2:
    print("Computer Choose paper" ,paper)


if user_choice == 0:
    print("User choose scissors" ,scissors)
elif user_choice == 1:
    print("User choose rock" ,rock)
elif user_choice ==2:
    print("User Choose paper" ,paper)
else:
    print("You typed an invalid")


if user_choice == computer_input:
    print("Round draw")                          #0 =scissorss
elif user_choice == 0 and computer_input==1:     #1 =rock
    print("Computer Won ")                       #2 =paper
elif user_choice == 0 and computer_input==2:
    print("User Won")
elif user_choice == 1 and computer_input==0:           #logic Correct 
    print("User won")                                             
elif user_choice == 1 and computer_input==2:
    print("Computer won")
elif user_choice == 2 and computer_input==0:
    print("Computer Won")
elif user_choice == 2 and computer_input==1:
    print("User won")






#game_images = [rock, paper, scissors]

#user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#if(user_choice>3 or user_choice<0):
    #print("You typed an invalid number")
#else:
    #print(game_images[user_choice])


#computer_choice = random.randint(0, 2)
#print("Computer chose:")
#print(game_images[computer_choice])

