import random

i = 0
parkings = []

while i < 15:
    parking = random.randint(0, 1)
    parkings.append(parking)
    i += 1

print(parkings)


