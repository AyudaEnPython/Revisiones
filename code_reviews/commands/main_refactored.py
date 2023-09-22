
help_commnads = """
start - to start the car
stop  - to stop the car
quit  - to exit
"""

command = ""
is_moving = False

while True:
    command = input("> ").lower()
    if command == "quit":
        break
    if command == "help":
        print(help_commnads)
    if command == "start":
        if is_moving:
            print("Car has already started")
        else:
            print("Car started") 
            is_moving = True
    elif command == "stop":
        if is_moving:
            print("Car stopped")
            is_moving = False
        else:
            print("Car has already stopped")
    else:
        print("Enter a valid command or type 'help'")

