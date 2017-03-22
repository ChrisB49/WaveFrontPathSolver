class Space:
    val = None
    leftSpace = None
    rightSpace = None
    upSpace = None
    downSpace = None

    def __init__(self, val=None):
        if val==None:
            print("This node is just a simple ")
        else:
            self.val = val

    def printVal(self):
        print(self.val, end=" ")

    def printUp(self):
        print(self.upSpace)

    def printDown(self):
        print(self.downSpace)

    def printRight(self):
        print(self.rightSpace)

    def printLeft(self):
        print(self.leftSpace)

    def setVal(self, val=None):
        if val==None:
            print("To set a value, you must pass a value......")
        else:
            self.val = val
        return


class Field:
    field = None
    start = (None,None)
    goal = (None,None)

    def __init__(self, rownum=None, colnum=None):
        if (rownum==None)or(colnum==None):
            print("The field is now empty of size(0,0)")
        else:
            self.field = [[Space(0) for x in range(colnum)] for y in range(rownum)]
        print()

    def linkSpaces(self):
        for i in range(self.field.__len__()):
            for x in range(self.field[i].__len__()):
                if i == 0:
                    if x == 0:
                        self.field[i][x].upSpace = None
                        self.field[i][x].leftSpace = None
                        self.field[i][x].downSpace = self.field[i + 1][x]
                        self.field[i][x].rightSpace = self.field[i][x + 1]
                    elif x == self.field[i].__len__() - 1:
                        self.field[i][x].leftSpace = self.field[i][x-1]
                        self.field[i][x].downSpace = self.field[i + 1][x]
                        self.field[i][x].upSpace = None
                        self.field[i][x].rightSpace = None
                    else:
                        self.field[i][x].leftSpace = self.field[i][x - 1]
                        self.field[i][x].downSpace = self.field[i + 1][x]
                        self.field[i][x].rightSpace = self.field[i][x + 1]
                        self.field[i][x].upSpace = None
                elif i == self.field.__len__() - 1:
                    if x == 0:
                        self.field[i][x].upSpace = self.field[i - 1][x]
                        self.field[i][x].leftSpace = None
                        self.field[i][x].downSpace = None
                        self.field[i][x].rightSpace = self.field[i][x + 1]
                    elif x == self.field[i].__len__() - 1:
                        self.field[i][x].leftSpace = self.field[i][x-1]
                        self.field[i][x].downSpace = None
                        self.field[i][x].upSpace = self.field[i-1][x]
                        self.field[i][x].rightSpace = None
                    else:
                        self.field[i][x].leftSpace = self.field[i][x - 1]
                        self.field[i][x].downSpace = None
                        self.field[i][x].upSpace = self.field[i-1][x]
                        self.field[i][x].rightSpace = self.field[i][x+1]
                else:
                    if x == 0:
                        self.field[i][x].upSpace = self.field[i - 1][x]
                        self.field[i][x].leftSpace = None
                        self.field[i][x].downSpace = self.field[i + 1][x]
                        self.field[i][x].rightSpace = self.field[i][x + 1]
                    elif x == self.field[i].__len__() - 1:
                        self.field[i][x].leftSpace = self.field[i][x-1]
                        self.field[i][x].downSpace = self.field[i + 1][x]
                        self.field[i][x].upSpace = self.field[i-1][x]
                        self.field[i][x].rightSpace = None
                    else:
                        self.field[i][x].leftSpace = self.field[i][x - 1]
                        self.field[i][x].downSpace = self.field[i+1][x]
                        self.field[i][x].upSpace = self.field[i-1][x]
                        self.field[i][x].rightSpace = self.field[i][x+1]
        return

    def makeStart(self, pos=(None,None)):
        if pos==(None,None):
            print("You need to enter a position for the starting spot.")
        else:
            if (self.start == (None,None)):
                if (pos[0] < self.field[0].__len__() and pos[0] >= 0) and (pos[1] < self.field.__len__() and pos[1] >= 0):
                    self.start = pos
                    self.field[pos[0]][pos[1]].setVal("S")
                    print("Setting the Start was successful.")
                else:
                    print("The coordinates you entered were not valid, please retry.")
                    return
            else:
                print("Sorry, the start has already been initialized.")
        return

    def makeGoal(self, pos=(None,None)):
        if pos==(None,None):
            print("You need to enter a position for the goal spot.")
        else:
            if (self.goal == (None,None)):
                if (pos[0] < self.field[0].__len__() and pos[0] >= 0) and (pos[1] < self.field.__len__() and pos[1] >= 0):
                    self.goal = pos
                    self.field[pos[0]][pos[1]].setVal("G")
                    print("Setting the Goal was successful.")
                else:
                    print("The coordinates you entered were not valid, please retry.")
                    return
            else:
                print("Sorry, the goal has already been initialized.")
        return

    def __repr__(self):
        return "Todo"


myField = Field(10,10)
myField.linkSpaces()
myField.makeStart((0,3))
myField.makeGoal((4,4))
print(myField.start[1])
print(myField)