# importing whole module
from tkinter import *
from tkinter.ttk import *

# time library is using to get the current system time
from time import strftime

# created by mywindow variable for displaying GUI(GRAPHICAL USER INTERFACE) window
myWindow = Tk()

#title is set in the window
myWindow.title('Clock')

# defined a function with name time()
def time():

    #strftime() function will return the current sytem time in the given format
	string = strftime('%d / %B / %Y\n%I : %M : %S %p')

    #passed current timeto lbl
	lbl.config(text=string)

    # last line refresh the text in label after every second.
	lbl.after(1000, time)

# lable is created. the background colour is black, text colour is cyan
# font family is algerian and the font size of lable is 40.
# the variable name for the label is lbl.
lbl = Label(myWindow, font=('Algerian', 40, 'bold'),
			background='black',
			foreground='cyan')

# Placing clock at the centre
# of the GUI window
lbl.pack(anchor='center')

# time() is called to get time 
time()

#last mainloop() function is called to run the application.
mainloop()

