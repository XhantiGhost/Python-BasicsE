command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
        print("the car has started")
    elif command == "stop":
        if not started:
            print("car has stopped already")
        else:
            started == False
        print("the car has stopped")
    elif command == "help":
        print("""
        start - to start car
        stop - to stop car 
        quit - to quit game
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand what you saying")
