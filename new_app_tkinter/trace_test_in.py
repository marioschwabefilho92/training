#! python3
# -*- coding: utf-8 -*-

import tkinter as tk

class entries_tester_app(tk.Tk):
    def __init__(self, frame_title):
        super().__init__()
        # Create a title for the frame
        self.title(frame_title)
        # Create a variable for holding the text in the Entry
        self.entry_text_var = tk.StringVar()
        self.entry_text_var.trace_add("write", self.change_button_text)
        # Create an Entry connected to the entry_text_var
        self.entry_box = tk.Entry(self, text=self.entry_text_var)
        # Create the button
        self.print_button = tk.Button(self, text = "PLACEHOLDER TEXT", command=self.print_text)
        # Put the button and the entry to the frame
        self.entry_box.pack()
        self.print_button.pack()
        
    def change_button_text(self, *args): # Note the args
        # Change the button text
        self.print_button.config(text=self.entry_text_var.get())
        
    def print_text(self):
        # Print the text to the console
        print("You entered: \"{}\"".format(self.entry_box.get()))
        
        
if __name__ == "__main__":
    root = entries_tester_app("Entry test")
    root.mainloop()