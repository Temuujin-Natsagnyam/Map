# This is a script which creates a map of variable dimensions
# and allows the user to move a character around that map.
import random
savefile = "savefile.txt"  # savefile

def terrain_static(map):
    map[2][2]="X"
    map[0][0]="O"
    map[3][3]= "G"
    return map
def terrain_random(map):
    for xc in range(4):
        for yc in range(4):
            chance = random.randint(1,10)
            if chance == 6 or chance == 3:
                map[xc][yc] = "X"
    map[3][3]= "G"
    return map
def seperate(word):  # function that takes a word and makes it a list of all the characters inside the word
    result = []
    for l in word:
        result.append(l)
    return result
def makemap(x, y):
    map = []  # declare empty array/ will be big list
    print("\n")  # new line for cleaner GUI
    # the array becomes a 2D array aka small lists inside a big list
    for z in range(0, y):  # y decides how many lists will go inside the big list, will be the vertical value of grid
        map.append(["O"] * x)  # x decides how long one small list will be, will be horizontal value for grid
    map = terrain_random(map)
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
def move(map, x, y, char, world):
    direction = (input("WASD : your next move?\n\n>>>\t"))
    print("\n")
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
    else:
        print("Remember it's WASD controls\n")
        #return ("Remember it's WASD controls")
    if world == 2:
        if px >= x:
            px = px - x
        elif py >= y:
            py = py - y
    elif world == 1:
        if px >= x or py >= y or px < 0 or py < 0:
            print("\nError! Turn off world bondaries for that!\n")
            return ("\nError! Turn off world bondaries for that!")
    if map[py][px] == "X":                                      #detects collision
        print(("\nSorry, you cannot go that way!\n"))
    if map[py][px] == "G":                                      #detects collision
        print(("You've reached the goal"))
        return (1)
    map[py][px] = char
    save(map)
    return 0
def main():
    x=int(4)
    y=int(4)
    char = ("P")
    world = int(1)
    map = makemap(x, y)
    map[0][0] = char  # map[y][x]
    save(map)
    readnshow(x,y)
    while True:
        win = move(map, x, y, char, world)
        if win == 1:
            break
        readnshow(x,y)
main()
brek = input() # this is just to stop the window from closing
