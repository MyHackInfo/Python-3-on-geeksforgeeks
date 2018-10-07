'''
    ## 1-Frame:->> It acts as a container to hold the widgets. It is used for grouping and organizing the widgets
    #############################################################################################################
    # formate of frame:->
            1->highlightcolor: To set the color of the focus highlight when widget has to be focused.
            2->bd: to set the border width in pixels.
            3->bg: to set the normal background color.
            4->cursor: to set the cursor used.
            5->width: to set the width of the widget.
            6->height: to set the height of the widget.

'''
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()

############################################################
'''
    ## 2-Label:->> It refers to the display box where you can put any text or image which can be updated any time as per the code.
    #######################################################################################################################
    ## format of Label:->
        1->bg: to set he normal background color.
        2->bg to set he normal background color.
        3->command: to call a function.
        4->font: to set the font on the button label.
        5->image: to set the image on the button.
        6->width: to set the width of the button.
        7->height” to set the height of the button.
'''
from tkinter import *
root = Tk()
w = Label(root, text='Hot all Time not batter!')
w.pack()
root.mainloop()
