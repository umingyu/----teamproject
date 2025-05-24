from tkinter import *
from tkinter.simpledialog import *


def get_input():
    
    window = Tk()
    window.geometry("700x500")

    label1 = Label(window, text="")
    label1.pack()

    value1 = askstring("미세먼지 ","지금 위치하고계신 지역을 적으세용(예: 서울, 부산 등)")


    window.destroy()
    return value1