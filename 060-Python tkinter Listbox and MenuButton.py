'''
    ## 1-Listbox:->> It offers a list to the user from which the user can accept any number of options.
    #################################################################################################
    # format of Listbox:->
        1->highlightcolor: To set the color of the focus highlight when widget has to be focused.
        2->bg: to set he normal background color.
        3->bd: to set the border width in pixels.
        4->font: to set the font on the button label.
        5->image: to set the image on the widget.
        6->width: to set the width of the widget.
        7->height: to set the height of the widget.


'''
from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1,'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()

##################################################################
'''
    ## 1-MenuButton:->> It is a part of top-down menu which stays on the window all the time. Every menubutton has its own functionality.
    ##################################################################33
    # format of MenuButton:->
        1->activebackground: To set the background when mouse is over the widget.
        2->activeforeground: To set the foreground when mouse is over the widget.
        3->bg: to set he normal background color.
        4->bd: to set the size of border around the indicator.
        5->cursor: To appear the cursor when the mouse over the menubutton.
        6->image: to set the image on the widget.
        7->width: to set the width of the widget.
        8->height: to set the height of the widget.
        9->highlightcolor: To set the color of the focus highlight when widget has to be focused.

'''
