from tkinter import *
from tkinter.ttk import *

from time import strftime

# Create a UI (User Inteface) for the clock
root = Tk()
root.title('Clock')

# Define a fucntion for the time
def time():
    # String representing date and time
    string = strftime("%H:%M:%S %p")
    # Label Configuration
    label.config(text=string)
    label.after(1000,time) # Call out time function for every second
    

# Create a label to store our clock
label = Label(root, font=('ds-digital', 60), background='black', foreground='green')
label.pack(anchor='center')

time()
mainloop()



 