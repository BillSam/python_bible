# Ask user for name

name = input("What's your name?: ")
print(name)

# Ask user for age : input is in str type

age = input("What's your age?: ")
print(age)
# Ask user for city

city = input("What city do you live in?: ")
# Ask user what they enjoy

love = input("What do you love doing?: ")
# create output text

output_string = "Your name is {} and you are {} years old. \nYou Live in {} and you love {}"
output = output_string.format(name, age, city, love)

# print output to screen
print(output)
