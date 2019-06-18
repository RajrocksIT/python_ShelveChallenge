import shelve

locations = shelve.open("locations")
vocabulary = shelve.open('vocabulary')

loc = '1'      # changed to a string
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == '0':   # changed to a string
        break
    else:

        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

locations.close()
vocabulary.close()