# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help draw a window and face graphic

# import everything from the graphics library
from graphics import *

def main():
    # open a new window 200x200 pixels
    newWin = GraphWin('Face')

    # draw a face
    bigFace = Circle(Point(100,100), 95)
    bigFace.setOutline('#b3b300')
    bigFace.setFill('#ffffe6')
    bigFace.draw(newWin)

    # draw an eyes countour

    eye1 = Circle(Point(50,75), 30)
    eye1.setOutline('black')
    eye1.setFill('#6699ff')
    eye1.draw(newWin)

    eye2 = eye1.clone()
    eye2.draw(newWin)
    eye2.move(100,0)

    # draw an eyes
    eye1 = Circle(Point(50,75), 20)
    eye1.setOutline('#ffff99')
    eye1.setFill('#ff00ff')
    eye1.draw(newWin)

    eye2 = eye1.clone()
    eye2.draw(newWin)
    eye2.move(100,0)

    # draw the retina
    eye3 = Circle(Point(50,74), 13)
    eye3.setOutline('#ff00ff')
    eye3.setFill('#66ccff')
    eye3.draw(newWin)

    eye4 = eye3.clone()
    eye4.draw(newWin)
    eye4.move(100,0)

    # draw an eyebraw
    eyebrow1 = Polygon(Point(85,45), Point(45,25), Point(85,25))
    eyebrow1.setFill('yellow')
    eyebrow1.draw(newWin)

    eyebrow2 = Polygon(Point(115,45), Point(115,25), Point(155,25))
    eyebrow2.setFill('yellow')
    eyebrow2.draw(newWin)

    # draw a nose
    nose1 = Rectangle(Point(85,85), Point(115,115))
    nose1.setOutline('white')
    nose1.setFill('#ffe6b3')
    nose1.draw(newWin)

    nose2 = Polygon(Point(90,110), Point(110,110), Point(110,90))
    nose2.setOutline('#ffe6b3')
    nose2.setFill('orange')
    nose2.draw(newWin)

    # draw a mouth
    mouth = Oval(Point(40,140), Point(165,165))
    mouth.setOutline('#660033')
    mouth.setFill('#ff8080')
    mouth.draw(newWin)

    # pause for click in window
    newWin.getMouse()

    # close/destroy the window
    newWin.close()

main()
