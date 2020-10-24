import tkinter as tk
from math import *
from tkinter import messagebox
from tkinter.ttk import *

def evaluate(event):
	res.configure(text="Result:" + str(eval(entry.get())))
root = tk.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator by suprith")

tk.Label(root, text="Enter your Expression:").pack()
entry = tk.Entry(root, width=50, background="ghost white")
entry.bind("<Return>", evaluate)
entry.pack(expand = False, fill = "both")
res = tk.Label(root, width=100, height=100, background="snow")
res.pack(expand = True, fill = "both")

root.mainloop()
