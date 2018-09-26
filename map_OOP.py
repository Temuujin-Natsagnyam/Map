import random
from tkinter import Button
from tkinter import *

def linear_search(field, target):
    for location in range(len(field)):
        if field[location] == target:
            return location
class map:
    savefile = "savefile.txt"
    damage = 0
    def __init__(self, length, width, character):
        self.length = length
        self.width = width
        self.character = character

        map = self.SetTerrain()
        map[width - 1][length - 1] = character  # map[y][x]
        self.SaveMap(map)

    def MakeMapArray(self):                                # Create 2d array
        map = []
        for z in range(0, self.width):
            map.append(["O"] * self.length)
        self.SaveMap(map)
    def SaveMap(self, map):
        savemap = []
        for row in map:
            savemap.append(''.join(tile for tile in row))  # Converting 2d array to 1d
            savemap.append('\n')                           # Joined all the tiles in the rows
        savemap = ''.join(row for row in savemap)          # Joined all the rows in the map

        savefile = open(self.savefile, 'w')                # Open save file and clesr previous save
        savefile.write(savemap)
        savefile.close()
    def LocateCharacter(self):
        savefile = open(self.savefile, 'r')
        for ctr in range(self.width):
            row = savefile.read(self.length + 1)
            x_found = linear_search(row, self.character)
            if x_found is not None:
                x = x_found
                y = ctr
        savefile.close()
        return x, y
    def DisplayMap(self):                                 #
        savefile = open(self.savefile, 'r')
        MapArray = []
        for t in range(self.width):
            row = savefile.read(self.length + 1).strip()
            MapArray.append(row)
        savefile.close()
        return ('\n'.join(MapArray))
    def LoadMap(self):                                     # 1d array to 2d
        savefile = open(self.savefile, 'r')
        MapArray = []
        for t in range(self.width):
            row = savefile.read(self.length + 1).strip()
            row = list(row)
            MapArray.append(row)
        savefile.close()
        return MapArray
    def moveup(self):
        maparray = self.LoadMap()
        self.damage = False
        x,y = self.LocateCharacter()
        maparray[y][x] = 'O'                               # Clear it's old position
        y -= 1

        if y >= self.width or y < 0:                       # Border Detection
            return maparray
        if maparray[y][x] == "G":                          # Collision detection
            self.damage = True
            return maparray
        else:
            maparray[y][x] = self.character
            self.SaveMap(maparray)

            return maparray
    def movedown(self):
        maparray = self.LoadMap()
        self.damage = False
        x,y = self.LocateCharacter()
        maparray[y][x] = 'O'                               # Clear it's old position
        y += 1

        if y >= self.width or y < 0:                       # Border Detection
            return maparray
        if maparray[y][x] == "G":                          # Collision detection
            self.damage = True
            return maparray
        else:
            maparray[y][x] = self.character
            self.SaveMap(maparray)

            return maparray
    def moveright(self):
        maparray = self.LoadMap()
        self.damage = False
        x,y = self.LocateCharacter()
        maparray[y][x] = 'O'                               # Clear it's old position
        x += 1

        if x >= self.length or x < 0:                       # Border Detection
            return maparray
        if maparray[y][x] == "G":                          # Collision detection
            self.damage = True
            return maparray
        else:
            maparray[y][x] = self.character
            self.SaveMap(maparray)

            return maparray
    def moveleft(self):
        maparray = self.LoadMap()
        self.damage = False
        x,y = self.LocateCharacter()
        maparray[y][x] = 'O'                               # Clear it's old position
        x -= 1

        if x >= self.length or x < 0:                       # Border Detection
            return maparray
        if maparray[y][x] == "G":                          # Collision detection
            self.damage = True
            return maparray
        else:
            maparray[y][x] = self.character
            self.SaveMap(maparray)

            return maparray
    def refresh(self):
        map = self.SetTerrain()
        map[self.width - 1][self.length - 1] = self.character
        self.SaveMap(map)
    def SetTerrain(self):
        self.MakeMapArray()
        maparray = self.LoadMap()
        terrainodds = [2,5,8]                      #30%
        for y in range(self.width):
            for x in range(self.length):
                chance = random.randint(1,10)
                if chance in terrainodds:
                    maparray[y][x] = 'G'
        maparray[0][0] = 'O'
        return maparray
    def CheckVictory(self):
        x,y = self.LocateCharacter()
        if x == 0 and y == 0:
            return 'gg'
    def CheckDamage(self, health):
        if self.damage is True:
            health -= 1
        healthpoints = "♥"*health
        healthpoints = ''.join(healthpoints)
        return healthpoints

def button_handler(event):
    widg = event.widget
    health = len(healthpoints.get())
    flag = 0
    if widg == restartbutton:
        text.delete("1.0", END)     #clear old text
        mappy.refresh()
        text.insert(END, mappy.DisplayMap())
        healthpoints.set("♥♥♥")
        flag = 1

    elif widg == upbutton:
        text.delete("1.0",END)
        maparray = mappy.moveup()
        text.insert(END, mappy.DisplayMap())
        healthpoints.set(mappy.CheckDamage(health))
    elif widg == downbutton:
        text.delete("1.0",END)
        maparray = mappy.movedown()
        text.insert(END, mappy.DisplayMap())
        healthpoints.set(mappy.CheckDamage(health))
    elif widg == rightbutton:
        text.delete("1.0",END)
        maparray = mappy.moveright()
        text.insert(END, mappy.DisplayMap())
        healthpoints.set(mappy.CheckDamage(health))
    elif widg == leftbutton:
        text.delete("1.0",END)
        maparray = mappy.moveleft()
        text.insert(END, mappy.DisplayMap())
        healthpoints.set(mappy.CheckDamage(health))

    if mappy.CheckVictory() == 'gg' and flag == 0:
        text.delete("1.0", END)
        text.insert(END, "YOU WIN")
    if health == 0 and flag == 0:
        text.delete("1.0", END)
        text.insert(END, "YOU DONT WIN")

mappy = map(10, 6, 'X')
app = Tk()
healthpoints = StringVar()
healthpoints.set("♥♥♥")
app.resizable(0,0)
app.title("Revision Speed Run")

text= Text(app,width=14,heigh=6, font=("Helvetica", 32),bg="black",fg="White")
text.grid(row=0,column=0,columnspan=5)

nothing = Button(app,text="Nothing")
nothing.grid(row=2,column=2)

upbutton=Button(app,text='Move up')
upbutton.grid(row=1,column=2)

downbutton=Button(app,text='Move down')
downbutton.grid(row=3,column=2)

rightbutton=Button(app,text='Move right')
rightbutton.grid(row=2,column=3)

leftbutton=Button(app,text='Move left')
leftbutton.grid(row=2,column=1)

restartbutton=Button(app,text="RESET")
restartbutton.grid(column=0,row=1)

healthbar = Label(app, textvariable=healthpoints, anchor=W, justify=LEFT, fg="red",bg="black", font=16, width= 4)
healthbar.grid(row=1,column=4)

app.bind('<Button-1>',button_handler)
app.mainloop()
