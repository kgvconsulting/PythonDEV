# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help finding perimeter and area of triangle by clicked three points using function

from graphics import *
import math

# define function for finding distance between two points
def distance(x1,x2,y1,y2):
    distanceTwoPoints = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distanceTwoPoints

# defining function for find triangle perimeter
def trianglePerimeter(a,b,c):
    perimeter = a + b + c
    return perimeter

# defining function for finding triangle area
def triangleArea(a,b,c):
    halfPerimeter = (a + b + c) / 2
    area = math.sqrt(halfPerimeter * (halfPerimeter - a) * (halfPerimeter - b) * (halfPerimeter - c))
    return area

# def main function for draw triangle by click on three points
def main():
    win = GraphWin("Draw a Triangle", 400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # get X,Y of the clicked points and finding triangle sides a, b and c
    xValueP1 = p1.getX()
    yValueP1 = p1.getY()

    xValueP2 = p2.getX()
    yValueP2 = p2.getY()

    xValueP3 = p3.getX()
    yValueP3 = p3.getY()

    # calling function distance() to find the triangle sides
    sideA = distance(xValueP1,xValueP2,yValueP1,yValueP2)
    sideB = distance(xValueP2,xValueP3,yValueP2,yValueP3)
    sideC = distance(xValueP3,xValueP1,yValueP3,yValueP1)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # call predefined functions trianglePerimeter() and triangleArea()
    trianP = trianglePerimeter(sideA,sideB,sideC)
    trianA = triangleArea(sideA,sideB,sideC)

    # output assign the result for perimeter and are to variable result
    result = "The perimeter is: " + str(trianP) + "\n The area is: " + str(trianA) + "\n"
    message.setText(result)

    # get the text entered and print the result
    win.getMouse()

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()

main()
