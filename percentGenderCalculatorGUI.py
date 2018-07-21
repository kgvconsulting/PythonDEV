# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program using GUI help display the percentages of males & females in the class, by user inputed data

from graphics import *


def main():

    # define window
    winCalculator = GraphWin('Percent Gender Calculator', 500, 500)
    winCalculator.setCoords(0.0, 0.0, 3.0, 3.0)
    winCalculator.setBackground('#e6ffe6')

    # set the GUI on the window
    frameText = Rectangle(Point(0.1,2), Point(2.9,2.7))
    frameText.setOutline('#006600')
    frameText.setFill('#ffffe6')
    frameText.draw(winCalculator)
    
    Text(Point(0.7,2.5), 'Enter the number of females in class: ').draw(winCalculator)
    inputEntryFemales = Entry(Point(2.1,2.5), 40).draw(winCalculator)
    Text(Point(0.7,2.2), 'Enter the number of males in class: ').draw(winCalculator)
    inputEntryMales = Entry(Point(2.1,2.2), 40).draw(winCalculator)

    # draw calculate button
    btnCalc = Circle(Point(1.5,1.5), 0.28)
    btnCalc.setOutline('red')
    btnCalc.setFill('#ff9980')
    btnCalc.draw(winCalculator)

    btnCalc1 = Circle(Point(1.5,1.5), 0.26)
    btnCalc1.setOutline('red')
    btnCalc1.draw(winCalculator)

    button = Text(Point(1.5,1.5),"Calculate It")
    button.setStyle("bold")
    button.setSize(15)

    button.draw(winCalculator)

    # wait for a mouse click
    winCalculator.getMouse()

    # perform calculations and conversations
    userEntryFemales = int(inputEntryFemales.getText())
    userEntryMales = int(inputEntryMales.getText())

    classTotal = userEntryFemales + userEntryMales
    malePercent = (userEntryMales / classTotal) * 100
    femalePercent = (userEntryFemales / classTotal) * 100

    # display output
    outFrameText = Rectangle(Point(0.1,0.25), Point(2.9,1.05))
    outFrameText.setOutline('#003cb3')
    outFrameText.setFill('#e6ffff')
    outFrameText.draw(winCalculator)

    infoText = Text(Point(1.5,0.9), 'The percentage of students in class are: ')
    infoText.setStyle("bold")
    infoText.draw(winCalculator)

    outputTextFemales = Text(Point(1.5,0.7),"")
    outputTextFemales.setStyle("bold")
    outputTextFemales.setSize(20)
    outputTextFemales.draw(winCalculator)

    extraTextFemals = Text(Point(2,0.7), "%  Females")
    extraTextFemals.setStyle("bold")
    extraTextFemals.setSize(20)
    extraTextFemals.draw(winCalculator)
    outputTextFemales.setText(int(femalePercent))

    outputTextMales = Text(Point(1.5,0.4),"")
    outputTextMales.setStyle("bold")
    outputTextMales.setSize(20)
    outputTextMales.draw(winCalculator)

    extraTextMales = Text(Point(1.92,0.4), "%  Males")
    extraTextMales.setStyle("bold")
    extraTextMales.setSize(20)
    extraTextMales.draw(winCalculator)
    outputTextMales.setText(int(malePercent))


    # display Quit button
    button.setText("Quit")

    # pause for click in window
    winCalculator.getMouse()

    # exit and destroy the window
    winCalculator.close()
    
main()
