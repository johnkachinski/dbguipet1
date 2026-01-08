import tkinter as t
from tkinter import *
from base import sessionlocal,text


def launch_add_form():
    v = []
    root1 = Tk()
    root1.title('Adding window')
    root1.geometry('700x550')
    label = ['Order Date','Barcode','Quantity','Customer ID']
    order_name = t.Entry(root1)
    barcode = t.Entry(root1)
    quantity = t.Entry(root1)
    customer_id = t.Entry(root1)
    form = [order_name, barcode, quantity, customer_id]
    k = 10
    for i in form:
        k+=10
        lbl = t.Label(root1,text=label[form.index(i)])
        lbl.pack(anchor = S, padx = k, pady = 5)
        i.pack(anchor = S, padx = k, pady = 5)
    def add_butt():
        for i in form:
          v.append(i.get())
        with sessionlocal() as session:
            session.execute(text(f'INSERT INTO orders (`Order Date`,Barcode,Quantity,`Customer ID`) VALUES ("{str(v[0])}",{int(v[1])},{int(v[2])},{int(v[3])})'))
            session.commit()
        root1.destroy()
    add_butt = t.Button(root1, text='Добавить', command=add_butt, width=10)
    add_butt.pack(anchor = S,fill = X)
    root1.mainloop()
