#! python3
import pyautogui
from tkinter import *
from PIL import ImageTk, Image

# budowa okienka
root = Tk() # tworzenie okna głównego
root.title("Mouse Coordinate")
root.iconbitmap("paint.ico")
logoImage = ImageTk.PhotoImage(Image.open("logo.png"))

def mouse():
    x, y = pyautogui.position()
    positionStr = 'X ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    return positionStr

def colorPixel():
    try:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        color = ' RGB: (' + str(pixelColor[0]).rjust(3)
        color += ', ' + str(pixelColor[1]).rjust(3)
        color += ', ' + str(pixelColor[2]).rjust(3) + ')'
        return color
    except IndexError:
        output =  ("poza skalą ")
        return output

# set first label text
mouseValue = StringVar(); mouseValue.set(mouse())
colorPixelValue = StringVar(); colorPixelValue.set(colorPixel())




# define labels
mouseCoordinate = Label(root, width=40 , textvariable = mouseValue, bd=1, relief=SUNKEN)
pixelColor = Label(root, width=40, textvariable = colorPixelValue, bd=1, relief=SUNKEN)
logo = Label(image=logoImage)


# Put labels on screen
mouseCoordinate.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
pixelColor.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

logo.grid(row=3, column=0, columnspan = 3)

# dynamical label refresh
while True:
    try:
        mouseValue.set(mouse())
        colorPixelValue.set(colorPixel())
        root.update()
    except TclError:
        sys.exit()