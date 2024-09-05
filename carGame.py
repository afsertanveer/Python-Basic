print('''start-to start the car
stop-to stop the car
quit- to terminate the program''')

flag = True
started = False
stopped = False
while flag:
    command = input("> ")
    if command.lower() == 'start':
        if started :
            print("Car is already Running")
        else:
            print("The Car is starting")
            started = True
            stopped = False
    elif command.lower() == 'stop' :
        if stopped :
            print("The car is already stopped")
        else:
            print("The Car is stopped")
            stopped = True
            started = False
    elif command.lower() == 'quit' :
        break