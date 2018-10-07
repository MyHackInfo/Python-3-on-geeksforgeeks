'''
    ### Python GUI – tkinter ###
    -Python offers multiple options for developing GUI (Graphical User Interface).
    -Out of all the GUI methods, tkinter is most commonly used method.
    -It is a standard Python interface to the Tk GUI toolkit shipped with Python.
    -Python with tkinter outputs the fastest and easiest way to create the GUI applications.
    -Creating a GUI using tkinter is an easy task.

    ## Create tkinter:
        1->Importing the module – tkinter
        2->Create the main window (container)
        3->Add any number of widgets to the main window
        4->Apply the event Trigger on the widgets.

    ## Two Main Methods that remember every time.
        1->Tk()
        2->mainloop()

    ## There are mainly three geometry manager classes class.
        1-> pack() method:It organizes the widgets in blocks before placing in the parent widget.
        2-> grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
        3-> place() method:It organizes the widgets by placing them on specific positions directed by the programmer.

'''
import tkinter

m = tkinter.Tk()

m.mainloop()
