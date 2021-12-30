from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *


# Color ConvertingRGB
def nero(rgb):
    return "#%02x%02x%02x" % rgb

# ApplicationClose


def close():
    main_screen.destroy()


def trapezoidal():
    global trapezoidal_screen
    trapezoidal_screen = Toplevel(main_screen)

    def back():
        trapezoidal_screen.destroy()

    trapezoidal_screen.geometry("560x680+350+0")
    trapezoidal_screen.configure(bg='#2C3A47')
    trapezoidal_screen.overrideredirect(1)

    Label(trapezoidal_screen, text="", background='#2C3A47').pack()
    btn = Button(trapezoidal_screen, padx=8, pady=4, fg='white', font=('Ubuntu', 14, 'bold'),
                 text="Back", command=back, bg='#1B9CFC', relief='flat', cursor="hand2").pack()

    path = "Trapezoidal.png"
    img = ImageTk.PhotoImage(Image.open(path).resize((350, 250)))
    panel = Label(trapezoidal_screen, image=img, highlightthickness=0,
                  bd=0, background='#2C3A47')
    panel.photo = img
    panel.pack()

    Label(trapezoidal_screen, text="Enter Equation: ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # x * x * x - 2 * x - 5
    eq = Entry(trapezoidal_screen, width="50")
    eq.pack()
    Label(trapezoidal_screen, text="", background='#2C3A47').pack()
    Label(trapezoidal_screen, text="Enter lower limit : ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # 1.9
    a = Entry(trapezoidal_screen, width="50")
    a.pack()
    Label(trapezoidal_screen, text="", background='#2C3A47').pack()
    Label(trapezoidal_screen, text="Enter upper limit : ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # 2
    b = Entry(trapezoidal_screen, width="50")
    b.pack()
    Label(trapezoidal_screen, text="", background='#2C3A47').pack()
    Label(trapezoidal_screen, text="Enter sub interval: ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # 2.1
    c = Entry(trapezoidal_screen, width="50")
    c.pack()
    Label(trapezoidal_screen, text="", background='#2C3A47').pack()

    def calculate():
        if a.get() == "" and b.get() == "" and c.get() == "":
            import ctypes
            ctypes.windll.user32.MessageBoxW(
                0, "Give The Guesses", "Status", 0)
        elif a.get() == "" or b.get() == "" or c.get() == "":
            import ctypes
            ctypes.windll.user32.MessageBoxW(
                0, "Give The Guesses", "Status", 0)
        else:
            equation = eq.get()
            eqn = sympify(equation)

            def func(x):
                return eqn.subs({'x': x})

            def trapezoidmethod(a, b, c):
                h = (b-a) / c
                integration = func(a) + func(b)
                for i in range(1, c):
                    k = a + i*h
                    integration = integration + 2 * func(k)
                integration = integration * h / 2
                ans = ("The integral of given equation is %0.6f" %
                       (integration))
                import ctypes
                ctypes.windll.user32.MessageBoxW(0, str(ans), "Answer", 0)

            a1 = float(a.get())
            b1 = float(b.get())
            c1 = int(c.get())
            trapezoidmethod(a1, b1, c1)
    btn = Button(trapezoidal_screen, padx=8, pady=4, fg='white', font=('Ubuntu', 14, 'bold'),
                 text="Calculate", command=calculate, bg='#1B9CFC', relief='flat', cursor="hand2").pack()
    Label(trapezoidal_screen, text="", background='#2C3A47').pack()


def simpson():
    global simp_screen
    simp_screen = Toplevel(main_screen)

    def back():
        simp_screen.destroy()
    simp_screen.geometry("560x680+350+0")
    simp_screen.configure(bg='#2C3A47')
    simp_screen.overrideredirect(1)

    Label(simp_screen, text="", background='#2C3A47').pack()
    # btn = Button(mull_screen, text="Back", command=back).pack()
    btn = Button(simp_screen, padx=8, pady=4, fg='white', font=('Ubuntu', 14, 'bold'),
                 text="Back", command=back, bg='#1B9CFC', relief='flat', cursor="hand2").pack()

    path = "simpson.png"
    img = ImageTk.PhotoImage(Image.open(path).resize((350, 250)))
    panel = Label(simp_screen, image=img, highlightthickness=0,
                  bd=0, background='#2C3A47')
    panel.photo = img
    panel.pack()

    Label(simp_screen, text="Enter Equation : ", background='#2C3A47',
          fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # x * x * x - 2 * x - 5
    eq = Entry(simp_screen, width="50")
    eq.pack()
    Label(simp_screen, text="", background='#2C3A47').pack()
    Label(simp_screen, text="Enter lower limit: ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # 1.9
    a = Entry(simp_screen, width="50")
    a.pack()
    Label(simp_screen, text="", background='#2C3A47').pack()
    Label(simp_screen, text="Enter upper limit: ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # 2
    b = Entry(simp_screen, width="50")
    b.pack()
    Label(simp_screen, text="", background='#2C3A47').pack()
    Label(simp_screen, text="Enter sub interval: ",
          background='#2C3A47', fg="#f7f1e3", font=("tahoma", 16, 'bold')).pack()  # 2.1
    c = Entry(simp_screen, width="50")
    c.pack()
    Label(simp_screen, text="", background='#2C3A47').pack()

    def calculate():
        if a.get() == "" and b.get() == "" and c.get() == "":
            import ctypes
            ctypes.windll.user32.MessageBoxW(
                0, "Give The Guesses", "Status", 0)
        elif a.get() == "" or b.get() == "" or c.get() == "":
            import ctypes
            ctypes.windll.user32.MessageBoxW(
                0, "Give The Guesses", "Status", 0)
        else:

            equation = eq.get()
            eqn = sympify(equation)
            def func(x): return eqn.subs({'x': x})

            def simpsonmethod(a, b, c):
                h = (b-a) / c
                integration = func(a) + func(b)
                for i in range(1, c):
                    k = a + i*h
                    if i % 2 == 0:
                        integration = integration + 2*func(k)
                    else:
                        integration = integration + 4*func(k)
                integration = integration * h/3
                ans = ("the value of integration is: %0.6f" % (integration))
                import ctypes
                ctypes.windll.user32.MessageBoxW(0, str(ans), "Status", 0)

            a1 = float(a.get())
            b1 = float(b.get())
            c1 = int(c.get())
            simpsonmethod(a1, b1, c1)

    btn = Button(simp_screen, padx=8, pady=4, fg='white', font=('Ubuntu', 14, 'bold'),
                 text="Calculate", command=calculate, bg='#1B9CFC', relief='flat', cursor="hand2").pack()
    Label(simp_screen, text="", background='#2C3A47').pack()


# MainScreen
global main_screen
main_screen = Tk()
main_screen.configure(bg="#2C3A47")
main_screen.geometry("635x480+350+50")
main_screen.overrideredirect(1)


Label(main_screen, text="                       ", background="#2C3A47",
      fg="white", font=("Calibri", 16)).grid(row=2, column=16)


# SOFTWARE NAME
Label(main_screen, text="                                    ",
      background="#2C3A47", fg="Yellow", font=("Aharoni", 15)).grid(row=4, column=16)
Label(main_screen, text="SOFTWARE PACKAGE OF INTEGRATION METHODS",
      background="#2C3A47", fg="#f49f1c", font=("Tahoma", 18, 'bold')).grid(row=6, column=16, padx=10)
Label(main_screen, text="By Farrukh Ahmed Khan and", background="#2C3A47",
      fg="white", font=("Aharoni", 14)).grid(row=16, column=16)
Label(main_screen, text="Muhammad Sarim Khan Bangash", background="#2C3A47",
      fg="white", font=("Aharoni", 14)).grid(row=19, column=16)


# BUTTONS
Label(main_screen, text="                                    ",
      background="#2C3A47", fg="Yellow", font=("Aharoni", 15)).grid(row=27, column=16)

btn = Button(main_screen, padx=8, pady=4, fg='white', font=('Ubuntu', 14, 'bold'),
             text="Simpson1/3 Method", command=simpson, bg='#1B9CFC', relief='flat', cursor="hand2").grid(row=29, column=16, padx=10, pady=10)


btn = Button(main_screen, padx=7, pady=4, fg='white', font=('Ubuntu', 14, 'bold'),
             text="Trepeziodal Method", command=trapezoidal, bg='#1B9CFC', relief='flat', cursor="hand2").grid(row=31, column=16)

btn = Button(main_screen, padx=6, pady=2, fg='white', font=('Ubuntu', 14, 'bold'),
             text="Exit", command=close, bg='#1B9CFC', relief='flat', cursor="hand2").grid(row=33, column=16, padx=10, pady=10)

# Label(main_screen, text="                                    ",
#       background="#2C3A47", fg="Yellow", font=("Aharoni", 15)).grid(row=5, column=16)


main_screen.mainloop()
