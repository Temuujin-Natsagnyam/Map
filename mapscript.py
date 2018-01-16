# This is a script which creates a map of variable dimensions
# and allows the user to move a character around that map.
savefile = "mapsave.txt"  # savefile


def menu():
    x, y = input("\nEnter size of map(x,y): e.g 10 10 \n").split()  # takes dimensions of map
    char = input("What is your favourite letter? ")  # takes character to use as main object
    char = char.upper()  # capitalises it

    return x, y, char  # returns all of it


def seperate(word):  # function that takes a word and makes it a list of all the characters inside the word
    result = []
    for l in word:
        result.append(l)
    return result


def init():  # initial setup function
    x, y, char = menu()  # gets values
    x = int(x)
    y = int(y)  # str -> int type
    map = makemap(x, y)  #
    return map, x, y, char  #


def makemap(x, y):
    map = []  # declare empty array/ will be big list
    print("\n")  # new line for cleaner GUI
    # the array becomes a 2D array aka small lists inside a big list
    for z in range(0, y):  # y decides how many lists will go inside the big list, will be the vertical value of grid
        map.append(["O"] * x)  # x decides how long one small list will be, will be horizontal value for grid
    for row in map:  # map is the big list, with lists inside it. row will iterate as each small list inside big list
        print("".join(row))  # prints out the row all connected.
        # for loop jumps to the nextline every iteration
    print("\n Map created of " + str(x) + " long, and " + str(y) + " wide\n")  # gui
    return map  # RETURNS ARRAY, not the map, but the array of it


def save(map):  # function used to save the progress onto an external txt file
    mapp = []  # declare empty array
    for row in range(len(map)):  # row iterates as each row of the grid // or each small list inside big list
        mapp.append(''.join(str(v) for v in map[row]))  # composite shortcut: it has a second loop
        # it joins all the little lists inside the big list, so the 2d array becomes a normal list
        mapp.append('\n')  # add a newline at each row orelse everything becomes one big line

    savemap = ''.join(str(a) for a in mapp)  # joins the remaining list

    fo = open(savefile, "w")  # open savefile and nuke it
    fo.write(savemap)  # save it
    fo.close()  # close it


def findxchar(row, char):  # func to locate character and returns its x coordinate position
    row = seperate(row)  # turns the row into a list of all its characters
    for xc in range(len(row)):  # checks every element in row // linear search
        if row[xc] == char:  # check
            return xc  # x coordinate of char


def locate(y, x, char):  # finds both coordinates of character from save file
    x = int(x)  # int type
    fo = open(savefile, "r+")  # open save file

    ctr = 0
    while ctr <= int(y):
        row = fo.read((x + 1)).strip()  # takes a line out of the save file
        tempx = findxchar(row, char)    # checks if that row contains character
        if tempx is not None:      # if it does have character that means it does not return None
            xc = tempx # in which case tempx is the x coordinate or xc
            yc = ctr# the ctr is also used to keep track of what line we are on, so the moment we find char we can say ctr is the vertical value
        ctr += 1
    fo.close()
    return xc, yc


def readnshow(x,y):
    x = int(x)  # int type
    fo = open(savefile, "r+")  # open save file

    ctr = 0
    while ctr <= int(y):
        row = fo.read((x + 1)).strip() # read a line from the save file
        print(row)     # print that
        ctr += 1   # each iteration goes to the next line
    fo.close()


def move(map, x, y, char):
    direction = (input("w to move up, s to move down, d to move right, a to move left.\n\n>>>\t"))
    px, py = locate(y, x, char)
    map[py][px] = "O"  # map[y][x]
    if direction == "d":
        px = px + 1
    elif direction == "a":
        px = px - 1
    elif direction == "s":
        py = py + 1
    elif direction == "w":
        py = py - 1

    map[py][px] = char
    save(map)


def main():
    map, x, y, char = init()
    map[0][0] = char  # map[y][x]
    save(map)
    readnshow(x,y)

    while True:
        move(map, x, y, char)
        readnshow(x,y)


main()
#not final one
