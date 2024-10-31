from tkinter import *

# Create the main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=100, height=100)
window.config(padx=20,pady=20)

def convert():
    entry1= float(entry.get()) * 1.60934
    label_k.config(text=f"{entry1}")
def reset():
    rest="0"
    label_k.config(text=rest)

# Create an Entry widget for user input
entry = Entry(width=10)
entry.grid(column=1,row=0,padx=20,pady=20) 


# Create a label for 'Miles'
label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)
# Create a text for conversion
text=Label(text="Convert to Kilometer")
text.grid(column=0,row=1)

# Creating the input for converted number
label_k = Label(text="0")
label_k.grid(column=1,row=1,padx=20,pady=20)
 

# Create a label for 'Kilo'
label_Kilo = Label(text="Kilo")
label_Kilo.grid(column=2,row=1)


# Create a button for submiting the input
button=Button(text="Convert",command=convert)
button.grid(column=1,row=2)

# Create a button for reset
reset=Button(text="Reset",command=reset)
reset.grid(column=2,row=2)


window.mainloop()
