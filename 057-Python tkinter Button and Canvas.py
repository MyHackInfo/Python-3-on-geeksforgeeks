'''
    ## 1- Button:->> To add a button in your application, this widget is used.

    ## format of the Buttons:>
        1->activebackground:-> to set the background color when button is under the cursor.
        2->activeforeground:-> to set the foreground color when button is under the cursor.
        3->bg:-> to set he normal background color.
        4->command:-> to call a function.
        5->font:-> to set the font on the button label.
        6->image:-> to set the image on the button.
        7->width:-> to set the width of the button.
        7->height:-> to set the height of the button.

'''
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()

############################
'''
    ## 2 Canvas:->> It is used to draw pictures and other complex layout like graphics, text and widgets.

    ## format of the Canvas:>>
        1->bd: to set the border width in pixels.
        2->bg: to set the normal background color.
        3->cursor: to set the cursor used in the canvas.
        4->highlightcolor: to set the color shown in the focus highlight.
        5->width: to set the width of the widget.
        6->height: to set the height of the widget.
'''
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
