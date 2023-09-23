
help_commnads = """
start - to start the car
stop  - to stop the car
quit  - to exit
"""
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "quit":
        break
    if command == "help":
        print(help_commnads)
    if command == "start":
        if started:
            print("Car has already started")
        else:
            print("Car started") 
            started = True
    elif command == "stop":
        if started:
            print("Car stopped")
            started = False
        else:
            print("Car has already stopped")
    else:
        print("Enter a valid command or type 'help'")

