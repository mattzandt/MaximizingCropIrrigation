
def main():
    # Retrieve input from file
    file = open('input.txt')
    inputList = file.read().splitlines()
    file.close()

    # Store information
    values = inputList[0].split()
    rows = int(values[0])
    columns = int(values[1])
    radius = int(values[2])

    # Iterate through field & find maximized position

    maxx = radius - 1
    maxy = radius
    maxcount = 0

    # Move sprinkler position
    for y in range(radius + 1, rows - radius):
        for x in range(radius, columns - radius - 1):
            # Count crops in radius
            count = 0

            for ry in range(y-radius, y+radius):
                for rx in range(x-radius, x+radius):
                    # Count crops that are within radius and are not the center
                    if ((ry-y)**2+(rx-x)**2) <= radius**2 and (inputList[ry][rx] == 'x') and not((ry == y) and (rx == x)):
                        count += 1

            # Check is location is a contender for max
            if count > maxcount:
                maxcount = count
                maxx = x
                maxy = y

    # Display results
    print('Maximized Position: (' + str(maxx) + ', ' + str(maxy-1) + ")\n" + "Crops in radius: " + str(maxcount))

    # Create a visual representation of the crops irrigated
    for ry in range(maxy-radius, maxy+radius):
                temp = list(inputList[ry])
                for rx in range(maxx-radius, maxx+radius):
                    # Check for center
                    if ry == maxy and rx == maxx:
                        temp[rx] = 'o'
                        inputList[ry] = ''.join(temp)
                    # Check if location is within radius
                    elif ((ry-maxy)**2+(rx-maxx)**2) <= radius**2:
                        # Check if crop...
                        if inputList[ry][rx] == 'x':
                            temp[rx] = '@'
                            inputList[ry] = ''.join(temp)
                        # ... or else it must be empty
                        else:
                            temp[rx] = ' '
                            inputList[ry] = ''.join(temp)

    # Output map with visual representation
    for i in range(1, rows):
        print(inputList[i])

if __name__ == '__main__':
    main()