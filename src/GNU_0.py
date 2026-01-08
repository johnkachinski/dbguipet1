import tkinter
from tkinter import *
from tkinter import ttk
from sqlalchemy import column
#from scripts import fetchall_orders
from GNU_1 import launch1

def button_start_comand():
  root = Tk()
  root.title('GNU base')
  root.geometry('700x550')
  def open_new_window():
      root.destroy()
      launch1()
  start_button = tkinter.Button(root,text = 'Начать',command = open_new_window, width = 25,height = 4)
  start_button.pack(expand = True)
  root.mainloop()
if __name__ == "__main__":
    button_start_comand()
