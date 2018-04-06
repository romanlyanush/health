import random

# Let's create a variable called 'Health' and give it a value of 50
health = 50
difficulty = 1

# to create a random number between 25 and 50 and save it as potion_health we
# need to use a pythons own random number generator and cast it as integer
potion_health = int(random.randint(25,50) / difficulty)

# using assignment operator '=' I am reassigning 'health' to the sum of
# 'current health' and 'potion_health'
health = health + potion_health

# print the new and updated value of health
print(health)
