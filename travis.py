known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

print(len(known_users))
i = 0
while i < len(known_users):
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {} " .format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == 'y':
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == 'n':
            print("No problem I didn't want you to leave ")
    else:
        print("Hmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added (y/n)?: ").strip().lower()
        if add_me == 'y':
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me == 'n':
            print("Sure! see you around")

    i += 1

