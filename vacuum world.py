def vacuum_world():
    rooms = {'A': 'Dirty', 'B': 'Dirty'}
    location = 'A'

    while 'Dirty' in rooms.values():
        print("Location:", location)
        print("Status:", rooms)

        if rooms[location] == 'Dirty':
            rooms[location] = 'Clean'
            print("Action: Suck")
        elif location == 'A':
            location = 'B'
            print("Action: Move Right")
        else:
            location = 'A'
            print("Action: Move Left")

    print("All rooms are clean!")
    print(rooms)

vacuum_world()
