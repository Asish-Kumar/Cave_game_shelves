# Author: Asish Kumar
# This is the actual logic behind the working of game
# Before running this, run "Caves_Initialise.py" at least once
import shelve

cave_file = shelve.open("Caves_locations")
locations = cave_file["locations"]
vocabulary = cave_file["vocabulary"]

loc = 1
while True:
    availableExits = ','.join(locations[loc]['exits'].keys())
    print(locations[loc]['desc'])
    if loc == 0:
        break
    else:
        allexits = locations[loc]['exits'].copy()
        allexits.update(locations[loc]['namedExits'])
    direction = input("Available exits are " + availableExits).upper()
    print()
    # parse the user input, using our vocabulary dictionary if necessary1
    if len(direction) > 1:  # more than one letter
        words = direction.split()
        for word in words:
            if word in vocabulary:  # does it contain a word we know
                direction = vocabulary[word]
                break
    if direction in allexits:
        loc = allexits[direction]
    else:
        print("Hye, you cannot go that way")

cave_file.close()
