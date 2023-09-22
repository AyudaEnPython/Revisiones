command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("car has already started")
        else:
            started=True
            print("car started")
    elif command=="stop":
        if not started:
            print("car stopped")
        else:
            started=False
            print("car has already stopped")
    elif command=="help":
            print(''' start–to start the car
            stop–to stop the car
            quit –to exit   ''')
    elif command=="quit":
        break
    else:
        print("i dont know what u are saying")