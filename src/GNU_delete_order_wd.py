import tkinter
import tkinter as t
from tkinter import *
from base import sessionlocal,text


def launch_delete_form():
    root1 = Tk()
    root1.title('Deleting window')
    root1.geometry('700x550')
    label =  tkinter.Label(root1,text='Order ID',width=10)
    label.pack(expand = True)
    order_id = t.Entry(root1)
    order_id.pack(expand = True)
    def add_butt():
        id = order_id.get()
        with sessionlocal() as session:
            session.execute(text(f'DELETE FROM orders WHERE `Order ID`={id}'))
            session.commit()
        root1.destroy()
    add_butt = t.Button(root1, text='Удалить', command=add_butt, width=10)
    add_butt.pack(expand = True,fill = X)
    root1.mainloop()