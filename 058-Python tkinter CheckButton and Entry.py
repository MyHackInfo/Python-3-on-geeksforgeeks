'''
    ## 1-CheckButton:->> To select any number of options by displaying a number of options to a user as toggle buttons.

    # format of this widget:>>
        1->Title: To set the title of the widget.
        2->activebackground: to set the background color when widget is under the cursor.
        3-activeforeground: to set the foreground color when widget is under the cursor.
        4-bg: to set he normal backgrouSteganography Break
        5-command: to call a function.
        6-font: to set the font on the button label.
        7-image: to set the image on the widget.

'''
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()

#########################################
'''
    ## 2-Entry:->> It is used to input the single line text entry from the user.. For multi-line text input, Text widget is used
    ############################################################################################################################
    # format of Entry:->
        1->bd: to set the border width in pixels.
        2->bg: to set the normal background color.
        3->cursor: to set the cursor used.
        4->command: to call a function.
        5->highlightcolor: to set the color shown in the focus highlight.
        6->width: to set the width of the button.
        7->height: to set the height of the button.

'''
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
