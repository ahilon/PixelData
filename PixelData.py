#! python3
import pyautogui
from tkinter import *
from PIL import ImageTk, Image

# Create window
root = Tk()
root.title("Mouse Coordinate")
root.iconbitmap("paint.ico")
logoImage = ImageTk.PhotoImage(Image.open("logo.png"))

# Functions
def mousePosition():
    x, y = pyautogui.position()
    positionStr =  str(x).rjust(4) + ' X ' + str(y).rjust(4)
    return positionStr

def positionRGB():
    try:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        color = '(' + str(pixelColor[0]).rjust(3)
        color += ',' + str(pixelColor[1]).rjust(3)
        color += ',' + str(pixelColor[2]).rjust(3) + ')'
        return color
    except IndexError:
        output =  ("Out of scale")
        return output

def positionHex():
    try:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        hex = "#{0:02x}{1:02x}{2:02x}".format(pixelColor[0],pixelColor[1], pixelColor[2])
        return hex
    except IndexError:
        output =  ("#F0F0F0")
        return output


# set values to function output
mousePositionValue = StringVar(); mousePositionValue.set(mousePosition())
positionRGBValue = StringVar(); positionRGBValue.set(positionRGB())
positionHexValue = StringVar(); positionHexValue.set(positionHex())

# define output labels
mousePositionLabel = Label(root, width=30, textvariable=mousePositionValue, bd=2, relief=GROOVE)
positionRGBLabel = Label(root, width=30, textvariable=positionRGBValue, bd=2, relief=GROOVE)
positionHexLabel = Label(root, width=30,  textvariable=positionHexValue, bd=2, relief=GROOVE)
positionColorLabel = Label(root, width=10, height= 5, bg=positionHex(), bd=2, relief=GROOVE)
#define text labels
resolutionTextLabel = Label(width=10, text='Resolution: ')
RGBTextLabel = Label(width=10, text='RGB: ')
hexTextLabel = Label(width=10, text='HEX: ')
#define logo label
logoLabel = Label(image=logoImage)

# Put output labels on screen
mousePositionLabel.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
positionRGBLabel.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
positionHexLabel.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
positionColorLabel.grid(row=3, column=0)
# Put text labels
resolutionTextLabel.grid(row=0, column=0)
RGBTextLabel.grid(row=1, column=0)
hexTextLabel.grid(row=2, column=0)
# Put logo label on screen
logoLabel.grid(row=3, column=1, columnspan=3)

# dynamical label refresh
while True:
    try:
        mousePositionValue.set(mousePosition())
        positionRGBValue.set(positionRGB())
        positionHexValue.set(positionHex())
        positionColorLabel.configure(background=positionHex())
        root.update()
    except TclError:
        sys.exit()