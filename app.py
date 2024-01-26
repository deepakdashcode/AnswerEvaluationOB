import tkinter as tk
import os

class App:
    def __init__(self, master):
        self.master = master
        master.title("Main App")

        self.label = tk.Label(master, text="This is the main app")
        self.label.pack()

        self.button = tk.Button(master, text="Open New Window", command=self.open_new_window)
        self.button.pack()

    def open_new_window(self):
        os.system("python gui.py")

root = tk.Tk()
app = App(root)
root.mainloop()
