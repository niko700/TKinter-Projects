#This code is to create a small Tkinter window that asks for a number and
#calculates what percentage it is of a larger number (hardcoded in).

from sys import argv
import tkinter as tk


#making tkinter window
window = tk.Tk()


#make greeting line
lbl_greeting = tk.Label(text = "What is your number?",
                    width = 20,
                    height = 5)
lbl_greeting.pack()


#making entry box
ent_entry = tk.Entry()
ent_entry.pack()

#what to do with entered text
string_number = ent_entry.get()


#making an "OK" button
btn_button = tk.Button(text = "OK",
                    width = 5,
                    height = 1)
btn_button.pack()


#define calculate restuls function
def convert(s):
    n = int(s)
    total = n/225*100
    return print(str(round(total,2)))


#button click event --> calculate what's in the box
def handle_click(event):
    output = convert(string_number)
    print(output)

btn_button.bind("<Button-1>", handle_click)


###make results text
##lbl_results = tk.Label(text = output_of_convert_function,
##                    width = 20,
##                    height = 5)
##lbl_results.pack()


#run the window
window.mainloop()