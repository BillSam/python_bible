import random

health = 50

difficulty = 1

# the more the difficulty less potion_health
potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print(health)
