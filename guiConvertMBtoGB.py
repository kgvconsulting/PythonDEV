# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help converting megabytes to gigabytes with GUI

from graphics import *

def main():
    winConvert = GraphWin("MB to GB Converter", 300, 300)
    winConvert.setCoords(0.0, 0.0, 3.0, 3.0)
    winConvert.setBackground('#e6ffe6')

    # set the GUI on the window
    frameText = Rectangle(Point(0.1,2.3), Point(2.9,2.7))
    frameText.setOutline('#006600')
    frameText.setFill('#ffffe6')
    frameText.draw(winConvert)

    Text(Point(1,2.5), 'Enter the MB to convert: ').draw(winConvert)
    inputMb = Entry(Point(2.1,2.5), 10).draw(winConvert)

    # draw calculate button
    btnConvert = Circle(Point(1.5,1.5), 0.32)
    btnConvert.setOutline('red')
    btnConvert.setFill('#ff9980')
    btnConvert.draw(winConvert)

    btnConvert1 = Circle(Point(1.5,1.5), 0.30)
    btnConvert1.setOutline('red')
    btnConvert1.draw(winConvert)

    button = Text(Point(1.5,1.5),"Convert")
    button.setStyle("bold")
    button.setSize(15)

    button.draw(winConvert)

    # wait for a mouse click
    winConvert.getMouse()

    # perform calculations and conversations
    userEntryMb = float(inputMb.getText())
    resultGb = userEntryMb / 1024

    # display output
    outFrameText = Rectangle(Point(0.1,0.20), Point(2.9,1.05))
    outFrameText.setOutline('#003cb3')
    outFrameText.setFill('#e6ffff')
    outFrameText.draw(winConvert)

    infoText = Text(Point(1.5,0.8), 'The coverted MB to GB are: ')
    infoText.setStyle("bold")
    infoText.draw(winConvert)

    outputTextMb = Text(Point(1.5,0.55),"")
    outputTextMb.setStyle("bold")
    outputTextMb.setSize(20)
    outputTextMb.draw(winConvert)

    outputTextMb.setText(float(round(resultGb,2)))

    # display Quit button
    button.setText("Quit")

    # pause for click in window
    winConvert.getMouse()

    # exit and destroy the window
    winConvert.close()
    
main()
