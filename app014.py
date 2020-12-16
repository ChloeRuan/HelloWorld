#  guessing game
secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1  # augmented assignment
    if guess == secret_num:
        print("You won!")
        break
else:
    print("Sorry, you failed")

    # exercise

command = ""
while command.lower() != "quit":
    command = input("Type here: ").lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
else:
    print("Sorry, I dont understand that")

command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
else:
    print("Sorry, I dont understand that")

#  how about if type "start' twice
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
        print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started == False
        print("Car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
else:
    print("Sorry, I dont understand that")
