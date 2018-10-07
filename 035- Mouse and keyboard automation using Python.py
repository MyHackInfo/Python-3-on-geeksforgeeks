'''
    #### Mouse and keyboard automation using Python ####
    -The pyautogui is a module that help us control mouse and keyboard with code.

    ## Some Functions
    1-size(): This function is used to get Screen resolution.
    2-moveTo(): use this function move the mouse in pyautogui module.
    3-moveRel() function: moves the mouse pointer relative to its previous position.
    4-position(): function to get current position of the mouse pointer.
    5-click(): Function used for clicking and dragging the mouse.
    6-scroll(): scroll function takes no. of pixels as argument, and scrolls the screen up to given number of pixels.
    7-typewrite(): You can automate typing of string by using typewrite() function. just pass the string which you want to type as argument of this function.

    * Passing key names: You can pass key names separately through typewrite() function.
    * Pressing hotkey combinations: Use hotkey() function to press combination of keys like ctrl-c, ctrl-a etc.


'''
import pyautogui

# Get screen size
print(pyautogui.size())

# Mouse move
pyautogui.moveTo(100,100,duration=1)

# previous position
pyautogui.moveRel(0,50,duration=1)

# Current Position
print(pyautogui.position())

# Mouse clicking
pyautogui.click(100,100)

# Scroll the screen
pyautogui.scroll(200)

# Type some text
pyautogui.typewrite("Hello Fuck World.")

# Hotkey
pyautogui.hotkey('ctrlleft','a')
