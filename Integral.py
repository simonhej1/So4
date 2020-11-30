import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import tkinter as tk
from tkinter import ttk

#a = float(input("hvad er a?:"))
#b = float(input("hvad er b?:"))
#c = float(input("hvad er c?:"))
#x = np.linspace(a, b, 100)

#y = np.sin(x)

#plt.figure()
#plt.plot(x, y)
#plt.show()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create widgets
        self.Inteknap = tk.Button(text = "Integralregning", command =self.calcInt)
        self.Difknap = tk.Button(text = "Differentialregning", command =self.calcDif)

        # place widgets
        self.Inteknap.pack(side="right")
        self.Difknap.pack(side="left")

    def calcDif(self):
        polynomial = input("To what degree?\n> ")
        polynomial = int(polynomial)
        if polynomial == 2:
            xPower = polynomial
            xPowerCoefficient = int(input("What is the coefficient of x^n?"))
            xCoefficient = int(input("What is the coefficient of x?"))
            newXPower = xPower - 1
            newXCoefficient = xCoefficient * xPower
            newXPower = str(newXPower)
            newXCoefficient = str(newXCoefficient)
            equation = newXCoefficient + "x" + newXPower + "+"
        elif polynomial == 3:
            pass
        elif polynomial == 4:
            pass
    def calcInt(self):
        pass
#create app
root = tk.Tk()
root.geometry("225x240")
app = Application(master=root)
app.master.frame()
app.master.title("Dif+Int Regning")

#start app
app.mainloop()