import tkinter as tk

class OurCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("DIP Calculator")

        self.label = tk.Label(self.root, text='Hello DIP01', font=('Arial', 18))
        self.label.pack()


        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('1'))
        self.button.place(x=0,y=30)

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('2'))
        self.button.place(x=60,y=30)

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('3'))
        self.button.place(x=120,y=30)
        
        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('4'))
        self.button.place(x=0,y=90)                 

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('5'))
        self.button.place(x=60,y=90)  

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('6'))
        self.button.place(x=120,y=90) 

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('7'))
        self.button.place(x=0,y=150) 

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('8'))
        self.button.place(x=60,y=150) 

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('9'))
        self.button.place(x=120,y=150) 

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('C'))
        self.button.place(x=0,y=210) 

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('0'))
        self.button.place(x=60,y=210)

        self.button = tk.Button(self.root, font=('Arial', 18), height=1,width=3 ,   text=('='))
        self.button.place(x=120,y=210)

        self.root.mainloop()
OurCalculator()