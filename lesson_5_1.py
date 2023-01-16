# import random
from random import choice, randint as generate_random_number  # alias
import calculator
from person import Person

from termcolor import cprint
import emoji
from decouple import config

print(generate_random_number(1, 5))
print(calculator.addition(8, 1))

friend = Person('Jim', 31)
print(f'My friend: ' + str(friend))

cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

db_url = config('DATABASE_URL')
print(db_url)

number = config('MY_NUMBER', cast=int)
print(number * 2)

commented_text = config('COMMENTED', default='Intead')
print(commented_text)
