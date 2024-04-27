print("Test")

import random

def draw_elements():
    elements=[]
    while len(elements)<4:
        number = random.randint(1,8)
        if number not in elements:
            elements.append(number)
    return elements

print(draw_elements())

print("sprobuj odgadnac haslo, podaj 4 liczby np. 1,2,3,4")
liczby_uzytkownika=input()
print("wprowadzone liczby to")
print(liczby_uzytkownika)

user_input = []
user_input = liczby_uzytkownika.split(",")

for i in range(len(user_input)):
    user_input[i] = int(user_input[i])

print(user_input)