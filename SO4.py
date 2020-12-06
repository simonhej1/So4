import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from Equation import Expression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.create_widgets()
        self.frame.pack()

    def create_widgets(self):
        self.button1 = tk.Button(self.frame, text = 'Luk', width = 25, command = self.Close)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Diffregning', width = 25, command = self.Diffregning)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text = 'Intregning', width = 25, command = self.Intregning)
        self.button3.pack()

    def Diffregning(self):
        self.Diffregning = tk.Toplevel(self.master)
        self.app = Window2(self.Diffregning)

    def Intregning(self):
        self.Intregning = tk.Toplevel(self.master)
        self.app = Window3(self.Intregning)

    def Close(self):
        self.master.destroy()

class Window2:
    def __init__(self, master):
        #initialisation
        self.master = master
        self.frame = tk.Frame(self.master)
        self.create_widgets()
        self.frame.pack()

    def create_widgets(self):
        #her laver jeg Labels og inputs og angiver properties
        self.funk = tk.Label(self.frame, text = 'Funktion:', width = 25)
        self.funkIn = tk.Entry(self.frame, width = 25)
        self.funkIn.insert(0, "7*x**2+12*x")
        self.x = tk.Label(self.frame, text='Indtast x', width=25)
        self.xIn= tk.Entry(self.frame, width=25)
        self.xIn.insert(0, "5")
        self.delX = tk.Label(self.frame, text='Indtast Delta X', width=25)
        self.delXIn = tk.Entry(self.frame, width=25)
        self.delXIn.insert(0, "2")

        #her "packer" jeg dem
        self.funk.pack()
        self.funkIn.pack()
        self.x.pack()
        self.xIn.pack()
        self.delX.pack()
        self.delXIn.pack()

        #man skal jo komme ud på en måde
        self.quitButton = tk.Button(self.frame, text = 'Tilbage', width = 25, command = self.close_window)
        self.quitButton.pack(side="right")

        self.Udregningknap = tk.Button(self.frame, text='Beregn!', width=25, command=self.Beregn)
        self.Udregningknap.pack(side="left")

    def Beregn(self):
        funk = Expression(self.funkIn.get(), "x")
        x = np.linspace(-30, 30, 1000)
        dx = x[1]-x[2]
        y = funk(x)

        fig, ax = plt.subplots()
        ax.plot(x, y, 'r', linewidth=1)
        ax.set_ylim(bottom=0)
        axes = plt.gca()
        axes.set_ylim([np.min(y), np.max(y)])
        plt.grid(True)

        X = float(self.xIn.get())
        dX = float(self.delXIn.get())
        for i in range(1000):
            if dX >= 0.0001:
                dX = dX / 2
            else:
                break

        dy = ((5 * (X + dX) * (X + dX) + 7 * (X + dX) + 10) - (5 * X * X + 7 * X + 10))
        diff = dy / dX

        self.plotWindow = tk.Toplevel(self.master)
        self.plotWindow.title("plotWindow")

        plot = FigureCanvasTkAgg(fig, self.plotWindow)
        plot.draw()
        plot.get_tk_widget().pack(side="bottom", fill="both", expand=1)

        self.plotLabel = tk.Label(self.plotWindow, text=("f(x)=", self.funkIn.get(), "\nDifferens for punktet x:", diff))
        self.plotLabel.pack(side="right")
        self.doneButton = tk.Button(self.plotWindow, text='Færdig', width=10, command=self.close_window)
        self.doneButton.pack(side="bottom")

    def close_window(self):
        self.master.destroy()

class Window3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.create_widgets()
        self.frame.pack()

    def create_widgets(self):
        self.funk = tk.Label(self.frame, text='Funktion:', width=25)
        self.funkIn = tk.Entry(self.frame, width=25)
        self.a = tk.Label(self.frame, text='Indtast a', width=25)
        self.aIn = tk.Entry(self.frame, width=25)
        self.b = tk.Label(self.frame, text='Indtast b', width=25)
        self.bIn = tk.Entry(self.frame, width=25)

        # her "packer" jeg dem
        self.funk.pack()
        self.funkIn.pack()
        self.a.pack()
        self.aIn.pack()
        self.b.pack()
        self.bIn.pack()

        # man skal jo komme ud på en måde
        self.quitButton = tk.Button(self.frame, text='Tilbage', width=25, command=self.close_window)
        self.quitButton.pack(side="right")

        # man skal jo beregne det på en måde
        self.Udregningknap = tk.Button(self.frame, text='Beregn!', width=25, command=self.Beregn)
        self.Udregningknap.pack(side="left")

    def Beregn(self):
        pass
    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()


if __name__ == '__main__':
    main()