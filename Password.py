#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []                                                              # great thinking mister jha im proud of you
for x in range (1,nr_letters+1):  
    text = random.choice(letters)
    password_list += text


for y in range(1,nr_symbols+1): 
    symbo = random.choice(symbols)     #string concatination
    password_list += symbo
    

for z in range(1,nr_numbers+1):
    num = random.choice(numbers)
    password_list += num
#print(password_list)
random.shuffle(password_list)
#print(password_list)

Pypassword = ""
  #### to onvert list to string use this metthod for sure
for char in password_list:
    Pypassword = Pypassword + char 

print(Pypassword)
    
   

   
