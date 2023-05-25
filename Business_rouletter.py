names = input(" Give everybody names who are sitting on the table ")

person = names.split(" ")

print(person)
total_person = len(person)
print(total_person)
import random
pick_a_number = random.randint(0,total_person-1)
print(pick_a_number)
print(person[pick_a_number])




