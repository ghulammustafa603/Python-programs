start = False
info = ""
while True:
    info = input(">").upper()
    if info == "START":
        if start:
            print("Car is already started")
        else:
            start = True
            print("Hey car started! Let's get ready to go!")
    elif info == "STOP":
        if start:
            start = False
            print("Hey car stopped!")
        else:
            print("Car is already stopped")
    elif info == "HELP":
        print("""
start - to start the car
stop - to stop the car       
quit - to terminate the program""")
    elif info == "QUIT":
        break
    else:
        print("Sorry! I don't understand")
