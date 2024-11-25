import tkinter as tk

class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget 

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)  

    def flush(self):
        pass 

