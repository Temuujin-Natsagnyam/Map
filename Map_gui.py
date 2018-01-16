from tkinter import *
import random
from tkinter import Button

savefile = "savefile.txt"
#-----------------------------------logic----------------------------------------------------------------
def seperate(word):  # function that takes a word and makes it a list of all the characters inside the word
    result = []
    for l in word:
        result.append(l)
    return result

def init():  # initial setup function
    char = "X"
    x = int(10)
    y = int(6)  # str -> int type
    map = makemap(x, y)  #
    return map, x, y, char  #

def makemap(x, y):
    map = []  # declare empty array/ will be big list
    #print("\n")  # new line for cleaner GUI
    # the array becomes a 2D array aka small lists inside a big list
    for z in range(0, y):  # y decides how many lists will go inside the big list, will be the vertical value of grid
        map.append(["O"] * x)  # x decides how long one small list will be, will be horizontal value for grid
    #for row in map:  # map is the big list, with lists inside it. row will iterate as each small list inside big list
        #print("".join(row))  # prints out the row all connected.
        # for loop jumps to the nextline every iteration
    #print("\n Map created of " + str(x) + " long, and " + str(y) + " wide\n")  # gui
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

    mappyboi = []

    ctr = 0
    while ctr <= int(y):
        row = fo.read((x + 1)).strip() # read a line from the save file
        mappyboi.append(row)     # print that
        ctr += 1   # each iteration goes to the next line
    fo.close()
    return str('\n'.join(mappyboi))

def mapfinder(x,y):
    x = int(x)  # int type
    fo = open(savefile, "r+")  # open save file

    mappyboi = []
    roww = []

    ctr = 0
    while ctr <= int(y):
        row = fo.read((x + 1)).strip() # read a line from the save file
        roww = seperate(row)
        mappyboi.append(roww)     # print that
        ctr += 1   # each iteration goes to the next line
    fo.close()

    return mappyboi

def moveup(map,x,y,char):


    px, py = locate(y, x, char)
    map[py][px] = "O"  # map[y][x]

    py = py - 1

    if px >= x or py >= y or px < 0 or py < 0:
        return map
    if map[py][px] == "G":
        return map
    else:
        map[py][px] = char

        save(map)

        return map

def movedown(map,x,y,char):
    px, py = locate(y, x, char)
    map[py][px] = "O"  # map[y][x]

    py = py + 1

    if px >= x or py >= y or px < 0 or py < 0:
        return map

    if map[py][px] == "G":
        return map


    map[py][px] = char

    save(map)

    return map

def moveright(map,x,y,char):
    px, py = locate(y, x, char)
    map[py][px] = "O"  # map[y][x]

    px = px + 1

    if px >= x or py >= y or px < 0 or py < 0:
        return map

    if map[py][px] == "G":
        return map


    map[py][px] = char

    save(map)

    return map

def moveleft(map,x,y,char):
    px, py = locate(y, x, char)
    map[py][px] = "O"  # map[y][x]

    px = px - 1

    if px >= x or py >= y or px < 0 or py < 0:
        return map

    if map[py][px] == "G":
        return map


    map[py][px] = char

    save(map)

    return map

def restard(map, x, y, char):
    px, py = locate(y, x, char)
    map[py][px] = "O"  # map[y][x]

    mapp, x, y, char = init()
    map, ctr = terrain(mapp)
    map[y-1][x-1] = char

    save(map)

    return map

def terrain(map):
    ctr = 0
    for xc in range(6):
        for yc in range(10):
            chance = random.randint(1,10)
            if chance == 6 or chance == 3 or chance==2:
                map[xc][yc] = "G"
                ctr += 1
    map[0][0]="O"
    map[5][9]= "O"
    return map, ctr

def victory(x,y,char):
    px, py = locate(x,y,char)

    if px == 0 and py == 0:
        return "gg"
    return None

map, x, y, char = init()
map, ctr = terrain(map)            ########################################################
map[y-1][x-1] = char  # map[y][x]
save(map)

#------------------------------GUI--------------------------------------------------------------

def button_handler(event):
    widg = event.widget

    if widg == restartbutton:
        text.delete("1.0", END)
        text.insert(END, readnshow(x, len(restard(mapfinder(x,y), x, y, char))))
    elif widg == upbutton:
        text.delete("1.0",END)
        text.insert(END,readnshow(x ,len(moveup(mapfinder(x,y), x, y, char))))
    elif widg == downbutton:
        text.delete("1.0",END)
        text.insert(END,readnshow(x ,len(movedown(mapfinder(x,y), x, y, char))))
    elif widg == rightbutton:
        text.delete("1.0",END)
        text.insert(END,readnshow(x ,len(moveright(mapfinder(x,y), x, y, char))))
    elif widg == leftbutton:
        text.delete("1.0", END)
        text.insert(END, readnshow(x, len(moveleft(mapfinder(x,y), x, y, char))))
    if victory(x, y, char) == "gg":
        text.delete("1.0", END)
        text.insert(END, "YOU WIN")
        #print("CHECk")

win = Tk()
win.resizable(0,0)
win.title("Map")

text= Text(win,width=14,heigh=6, font=("Helvetica", 32),bg="black",fg="White")
text.grid(row=0,column=0,columnspan=5)

nothing = Button(win,text="Nothing")
nothing.grid(row=2,column=2)

upbutton=Button(win,text='Move up')
upbutton.grid(row=1,column=2)

downbutton=Button(win,text='Move down')
downbutton.grid(row=3,column=2)

rightbutton=Button(win,text='Move right')
rightbutton.grid(row=2,column=3)

leftbutton=Button(win,text='Move left')
leftbutton.grid(row=2,column=1)

restartbutton=Button(win,text="RESET")
restartbutton.grid(column=0,row=1)

win.bind('<Button-1>',button_handler)

win.mainloop()