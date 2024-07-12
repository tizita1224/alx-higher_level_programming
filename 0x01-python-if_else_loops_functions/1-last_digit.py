#!/usr/bin/python3
import random


number = random.randint(-10000, 10000)

last_D = abs(number) % 10

if number < 0:
    last_D = abs(number) % -10

if last_D > 5:
    print(f"Last digit of {number} is {last_D} and is greater than 5")
elif last_D == 0:
    print(f"Last digit of {number} is {last_D} and is 0")
elif last_D < 6 and last_D != 0:
    print(f"Last digit of {number} is {last_D} and is less than 6 and not 0")
