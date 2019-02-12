from graphics import *
from button import Button


class Calculator:
    def __init__(self):
        self.win = win = GraphWin("Calculator", 500, 500)
        win.setCoords(0,0,6,7)
        win.setBackground("slategrey")
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        self.buttons = []
        # create a list with button speciffications(possition and label)
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')]
        # iterate through the list of specs and create a button for each spec.
        # append the newly created button to the list of buttons
        for (x,y,label) in bSpecs:
            self.buttons.append(Button(self.win, Point(x,y), 0.75, 0.75, label))
        # append the bigger('=') button
        self.buttons.append(Button(self.win, Point(4.5,1), 1.5, 0.75, "="))
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        disp = Rectangle(Point(1-0.375,5), Point(5.375,6))
        disp.setFill('white')
        disp.draw(self.win)
        text = Text(Point(3,5.5), "")
        text.setSize(25)
        text.setStyle("bold")
        text.draw(self.win)
        self.display = text

    def run(self):
        while True:
            key = self.getPressKey()
            self.proccessKey(key)

    def getPressKey(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel().getText()  # de ce e nevoie de .getText() ?????????????

    def proccessKey(self, key):
        text = self.display.getText()
        if key == "<-":
            self.display.setText(text[:-1])
        elif key == "C":
            self.display.setText("")
        elif key == "=":
            try:
                self.display.setText(str(eval(text)))
            except:
                self.display.setText("ERROR")
        else:
            self.display.setText(text + key)
    

if __name__ == "__main__":
    c = Calculator()
    c.run()
