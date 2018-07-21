# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help draw a house in GUI

# import everything from the graphics library
from graphics import *
import random

def colorM(color='yellow'):
    if color is 'green':
        circleColor = color_rgb(random.randrange(36, 125),
                random.randrange(80, 128),
                random.randrange(0, 5))

    elif color is 'purple':
        circleColor = color_rgb(random.randrange(82, 244),
                random.randrange(0, 5),
                random.randrange(77, 215))

    else:
        circleColor = color_rgb(random.randrange(215, 255),
                random.randrange(215, 255),
                random.randrange(0, 5))

    return circleColor

# main graphics
def main():
    #set the window and background
    newWin = GraphWin('House', 400, 400)
    newWin.setBackground('#e6ffff')

    # set ground background
    ground = Rectangle(Point(10,200), Point(390,390))
    ground.setFill('#00b300')
    ground.draw(newWin)

    # set house
    house = Rectangle(Point(175,140), Point(365,325))
    house.setFill('#ffa64d')
    house.draw(newWin)

    # set windows
    window = Rectangle(Point(210,170), Point(270,240))
    window.setOutline('#00e6e6')
    window.setFill('#e6ffff')
    window.draw(newWin)

    windowLineH = Line(Point(212,205), Point(268,205))
    windowLineH.setFill('#00e6e6')
    windowLineH.draw(newWin)

    windowLineV = Line(Point(240,170), Point(240,240))
    windowLineV.setFill('#00e6e6')
    windowLineV.draw(newWin)

    # set roof
    roof = Polygon(Point(370,140), Point(270,70), Point(170,140))
    roof.setFill('red')
    roof.draw(newWin)

    # set door
    doorFrame = Rectangle(Point(290,320), Point(340,230))
    doorFrame.setFill('black')
    doorFrame.draw(newWin)

    door = Rectangle(Point(288,318), Point(338,228))
    door.setFill('#993300')
    door.draw(newWin)

    doorHandle = Circle(Point(298,280), 4)
    doorHandle.setOutline('white')
    doorHandle.setFill('#00ace6')
    doorHandle.draw(newWin)

    # set fence
    fence = Rectangle(Point(165,390), Point(185,305))
    fence.setOutline('#e6e6e6')
    fence.setFill('#0099ff')
    fence.draw(newWin)

    fence1 = fence.clone()
    fence1.draw(newWin)
    fence1.move(21,0)

    fence2 = fence.clone()
    fence2.draw(newWin)
    fence2.move(42,0)

    fence3 = fence.clone()
    fence3.draw(newWin)
    fence3.move(63,0)

    # walk path
    path = Rectangle(Point(290,325), Point(339,389))
    path.setFill('white')
    path.draw(newWin)

    pathBlock = Rectangle(Point(289,325), Point(299,335))
    pathBlock.setFill('gray')
    pathBlock.draw(newWin)

    pathBlock1 = pathBlock.clone()
    pathBlock1.draw(newWin)
    pathBlock1.move(11,0)

    pathBlock2 = pathBlock.clone()
    pathBlock2.draw(newWin)
    pathBlock2.move(22,0)

    pathBlock3 = pathBlock.clone()
    pathBlock3.draw(newWin)
    pathBlock3.move(33,0)

    pathBlock4 = pathBlock.clone()
    pathBlock4.draw(newWin)
    pathBlock4.move(44,0)

    pathBlock21 = pathBlock.clone()
    pathBlock21.draw(newWin)
    pathBlock21.move(0,11)

    pathBlock22 = pathBlock.clone()
    pathBlock22.draw(newWin)
    pathBlock22.move(11,11)

    pathBlock23 = pathBlock.clone()
    pathBlock23.draw(newWin)
    pathBlock23.move(22,11)

    pathBlock24 = pathBlock.clone()
    pathBlock24.draw(newWin)
    pathBlock24.move(33,11)

    pathBlock25 = pathBlock.clone()
    pathBlock25.draw(newWin)
    pathBlock25.move(44,11)

    pathBlock31 = pathBlock.clone()
    pathBlock31.draw(newWin)
    pathBlock31.move(0,22)

    pathBlock32 = pathBlock.clone()
    pathBlock32.draw(newWin)
    pathBlock32.move(11,22)

    pathBlock33 = pathBlock.clone()
    pathBlock33.draw(newWin)
    pathBlock33.move(22,22)

    pathBlock34 = pathBlock.clone()
    pathBlock34.draw(newWin)
    pathBlock34.move(33,22)

    pathBlock35 = pathBlock.clone()
    pathBlock35.draw(newWin)
    pathBlock35.move(44,22)

    pathBlock41 = pathBlock.clone()
    pathBlock41.draw(newWin)
    pathBlock41.move(0,33)

    pathBlock42 = pathBlock.clone()
    pathBlock42.draw(newWin)
    pathBlock42.move(11,33)

    pathBlock43 = pathBlock.clone()
    pathBlock43.draw(newWin)
    pathBlock43.move(22,33)

    pathBlock44 = pathBlock.clone()
    pathBlock44.draw(newWin)
    pathBlock44.move(33,33)

    pathBlock45 = pathBlock.clone()
    pathBlock45.draw(newWin)
    pathBlock45.move(44,33)

    pathBlock50 = pathBlock.clone()
    pathBlock50.draw(newWin)
    pathBlock50.move(-11,44)

    pathBlock51 = pathBlock.clone()
    pathBlock51.draw(newWin)
    pathBlock51.move(0,44)

    pathBlock52 = pathBlock.clone()
    pathBlock52.draw(newWin)
    pathBlock52.move(11,44)

    pathBlock53 = pathBlock.clone()
    pathBlock53.draw(newWin)
    pathBlock53.move(22,44)

    pathBlock54 = pathBlock.clone()
    pathBlock54.draw(newWin)
    pathBlock54.move(33,44)

    pathBlock55 = pathBlock.clone()
    pathBlock55.draw(newWin)
    pathBlock55.move(44,44)

    pathBlock61 = pathBlock.clone()
    pathBlock61.draw(newWin)
    pathBlock61.move(-11,55)

    pathBlock62 = pathBlock.clone()
    pathBlock62.draw(newWin)
    pathBlock62.move(0,55)

    pathBlock63 = pathBlock.clone()
    pathBlock63.draw(newWin)
    pathBlock63.move(11,55)

    pathBlock64 = pathBlock.clone()
    pathBlock64.draw(newWin)
    pathBlock64.move(22,55)

    pathBlock65 = pathBlock.clone()
    pathBlock65.draw(newWin)
    pathBlock65.move(33,55)

    pathBlock66 = pathBlock.clone()
    pathBlock66.draw(newWin)
    pathBlock66.move(44,55)

    # set flowers

    flower0 = Circle(Point(275,340), 10)
    flower0.setFill('#ff66ff')
    flower0.draw(newWin)

    flower1 = Circle(Point(255,340), 10)
    flower1.setFill('#ff66ff')
    flower1.draw(newWin)

    flower2 = Circle(Point(265,320), 10)
    flower2.setFill('#ff66ff')
    flower2.draw(newWin)

    flower3 = Circle(Point(266,330), 10)
    flower3.setOutline('#ffff1a')
    flower3.setFill('#660066')
    flower3.draw(newWin)

    flower3 = Circle(Point(266,330), 5)
    flower3.setOutline('#ffff1a')
    flower3.setFill('#ff9933')
    flower3.draw(newWin)

    flowerStem3 = Line(Point(265,340), Point(265,375))
    flowerStem3.setFill('#004d1b')
    flowerStem3.draw(newWin)

    flowerLeaf3 = Oval(Point(265,365), Point(290,355))
    flowerLeaf3.setFill('#004d1b')
    flowerLeaf3.draw(newWin)

    flowerLeaf31 = flowerLeaf3.clone()
    flowerLeaf31.draw(newWin)
    flowerLeaf31.move(-25,0)

    # set tree
    for i in range(500):
        tree = Rectangle(Point(65,180), Point(75,275))
        tree.setOutline('#e6e6e6')
        tree.setFill('#663300')
        tree.draw(newWin)

        treeCrown = Oval(Point(40,130), Point(100,210))

        treeColor = colorM('green')
        treeCrown.setFill(treeColor)
        treeCrown.draw(newWin)

    # set sun
    for i in range(500):
        sun = Circle(Point(55,45), 35)
        
        circleColor = colorM()

        sun.setFill(circleColor)
        sun.setOutline('#e6e600')
        sun.draw(newWin)

    # pause for click in window
    newWin.getMouse()

    # close/destroy the window
    newWin.close()

main()
