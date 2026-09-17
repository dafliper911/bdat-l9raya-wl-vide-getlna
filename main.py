# Git: status → add → commit → push
import random

luck = 0
commands = ["evade", "attack", "run", "exit"]
running = True
ehp = 100

for command in commands:
    print("- " + command)

while running == True:

    user_input = input("what do you like to do ? : ")

    if user_input not in commands:
        print("not an option")

    elif user_input == "evade":
        random_number = random.randint(0, 100)

        if random_number + luck > 40:
            print("evaded")
            luck += 5
        else:
            print("died")
            luck -= 10
        print(random_number)
        print(luck)
        print(ehp)
    elif user_input == "attack":
        random_number = random.randint(0, 100)

        if random_number + luck > 70:
            print("attacked")
            luck += 4
            ehp -=  57
        else:
            print("died")
            luck -=10

        print(random_number)
        print(luck)
        print(ehp)
    elif user_input == "run":
        random_number = random.randint(0, 100)

        if random_number + luck > 30:
            print("you ran")
        else:
            print("died")
    if ehp <= 0:
        print("you won")
        running = False