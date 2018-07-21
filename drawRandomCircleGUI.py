# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help draw a window and random circles whit random colors graphic

# import everything from the graphics library
from graphics import *
import random

# define a empty function
def main():

    # open a new window 400x400 pixels
    newWin = GraphWin('RandomWindow', 400,400)

    # set window background
    newWin.setBackground('#ffffe6')

    #draw circles random
    circles = []
    for i in range(50):
        pointX = random.randrange(5, 395)
        pointY = random.randrange(5, 395)
        circleRadius = random.randrange(3, 65, 15)

        pointCircle = Circle(Point(pointX, pointY), circleRadius)

        #circles random color
        circleColor = color_rgb(random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255))

        pointCircle.setFill(circleColor)

        # draw circles in the window
        pointCircle.draw(newWin)

        # add new circle to the empty list
        circles.append(pointCircle)

    # pause for click in window
    newWin.getMouse()

    # close/destroy the window
    newWin.close()

# call the function
main()
