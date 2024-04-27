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
