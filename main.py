import tkinter as tk

class OurCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("DIP Calculator")

        self.label = tk.Label(self.root, text='Hello DIP01', font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root,text=('click here'))
        self.button.place(x=0,y=0)

        self.root.mainloop()
OurCalculator()