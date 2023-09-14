"""
Date: 09/02/23
Author: niko700
Edits: 
        - 09/13/23  - moved string variable into button click function
                    - created second parameter, but gave it a default value because still testing input process
                    - edited header
                    - formatted questions as """ """ strings

 Code Purpose:  

 This code is to create a small Tkinter window that asks for a number and
 calculates what percentage it is of a larger number (hardcoded in.
 
 Tried to incorporate some code from this example: https://insolor.github.io/effbot-tkinterbook-archive/entry.htm

 
Results:

Still get error where the entry window returns an empty string.

"""


from sys import argv
import tkinter as tk


#making tkinter window
window = tk.Tk()


#make greeting line
lbl = tk.Label(text = "What is your number?",
                    width = 20,
                    height = 5)
lbl.pack()


#declare string variable 
string = tk.StringVar()

#create entry widget
ent = tk.Entry(textvariable=string)
ent.pack()

# string.set("")
# out_string = string.get() 
"""do I keep this (above)? or is this made obsolete by the btn.out_string inside the function? also, switch this places with the entry widget, so it's closer to the declaration?"""


#making an "OK" button
btn = tk.Button(text = "OK",
                    width = 5,
                    height = 1)
btn.pack()


#make output line
lbl = tk.Label(text = "",
                        width = 20,
                        height = 3)
lbl.pack()


#define calculate results function
def convert(s1, s2="225"):
    n1 = int(s1)
    n2 = int(s2)
    total = n1/n2*100
    string_total = str(round(total,2))
    print(string_total) #to check while running
    # print(type(string_total))
    return string_total


#button click event --> calculate what's in the box
def handle_click(event):
    btn.out_string = string.get()   
    """so, this is creating an instance variable here, with btn.out_string being the object?"""
    """also, this equals expression does not need to be reversed? if because you are trying to get the variable to equal to the output of the button, not the other way around?"""
    
    print("You typed: " + btn.out_string)
    
    #calculate percent using convert() function
    total = convert(btn.out_string)
    # print(type(total))
    
    #create display text using result above
    to_display = "You're " + total + " % done!"
    lbl.configure(text = to_display)

btn.bind("<Button-1>", handle_click)


#run the window
window.mainloop()