films = {
    "Found jDory": [3, 5],
    "Find Dory": [3, 5],
    "Finding Dory": [3, 5],
    "Less Dory": [3, 5],
    "More Dory": [3, 5],

}

loops = len(films)
i = 0
while i <= loops:
    choice = input("What film?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age
        if age >= films[choice][0]:

            # check enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film")
                films[choice] = films[choice][1] - 1
        else:
            print("You too young to watch")
    else:
        print("We dnt have that film")
    i += 1
