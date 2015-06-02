
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
                    if (inputList[ry][rx] == 'x') and not((ry == y) and (rx == x)):
                        count += 1

            if count > maxcount:
                maxcount = count
                maxx = x
                maxy = y

    print('Maximized Position: (' + str(maxx+1) + ', ' + str(maxy) + ")")



if __name__ == '__main__':
    main()