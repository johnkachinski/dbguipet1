import tkinter
from tkinter import *
from tkinter import ttk
from scripts import fetchall_orders, get_customer_id
from GNU_add_order_wd import launch_add_form
from GNU_delete_order_wd import launch_delete_form

def launch1():
    root = Tk()
    root.title('GNU base')
    root.geometry('700x480')
    tree = ttk.Treeview(root, columns=('Order ID', 'Order Date', 'Barcode', 'Quantity', 'Customer ID'), show='headings',
                        height=10)
    tree.heading('Order ID', text='Order ID')
    tree.heading('Order Date', text='Order Date')
    tree.heading('Barcode', text='Barcode')
    tree.heading('Quantity', text='Quantity')
    tree.heading('Customer ID', text='Customer ID')
    tree.column('Order ID', width=80)
    tree.column('Order Date', width=80)
    tree.column('Barcode', width=80)
    tree.column('Quantity', width=80)
    tree.column('Customer ID', width=80)
    orders = []
    for i in fetchall_orders():
        orders.append([i[0], i[1], i[2], i[3], i[4]])
    for i in orders:
        tree.insert('', tkinter.END, values=i)
    def add_new_order():
        root.destroy()
        launch_add_form()
        launch1()
    def delete_order():
        root.destroy()
        launch_delete_form()
        launch1()
    def find_spec_el():
        launch2(cid.get())
    tree.pack(anchor=tkinter.NW, padx=10, pady=10)
    add_order_button = tkinter.Button(root, text='Добавить', command=add_new_order, width=10)
    add_order_button.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    lll = Label(root,text='Customer ID')
    lll.pack(anchor = tkinter.NE, padx = 1, pady = 1)
    cid = Entry(root)
    cid.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    find_el_button = tkinter.Button(root,text = 'Найти', command=find_spec_el,width = 10)
    find_el_button.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    delete_order_button = tkinter.Button(root, text='Удалить', command=delete_order, width=10)
    delete_order_button.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    def closemain():
        root.destroy()
    close = tkinter.Button(root, text='Закрыть',command=closemain, width=10)
    close.pack(anchor = tkinter.S)
    root.mainloop()
def launch2(customer_id):
    root1 = Tk()
    root1.title('Finding')
    root1.geometry('700x550')
    tree = ttk.Treeview(root1, columns=('Order ID', 'Order Date', 'Barcode', 'Quantity', 'Customer ID'), show='headings',
                        height=10)
    tree.heading('Order ID', text='Order ID')
    tree.heading('Order Date', text='Order Date')
    tree.heading('Barcode', text='Barcode')
    tree.heading('Quantity', text='Quantity')
    tree.heading('Customer ID', text='Customer ID')
    tree.column('Order ID', width=80)
    tree.column('Order Date', width=80)
    tree.column('Barcode', width=80)
    tree.column('Quantity', width=80)
    tree.column('Customer ID', width=80)
    orders = []
    for i in get_customer_id(customer_id):
        orders.append([i[0], i[1], i[2], i[3], i[4]])
    for i in orders:
        print(i)
        tree.insert('', tkinter.END, values=i)
    #def add_new_order():
       # root.destroy()
        #launch_add_form()
        #launch1()
    #def find_spec_el():
        #launch2(cid.get())
        #root.destroy()
    tree.pack(anchor=tkinter.NW, padx=10, pady=10)
    def close():
        root1.destroy()
    bbt = tkinter.Button(root1, text='Закрыть', command=close, width=10)
    bbt.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    #add_order_button = tkinter.Button(root, text='Добавить', command=add_new_order, width=10)
    #add_order_button.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    #cid = Entry(root)
    #cid.pack(anchor=tkinter.NE, padx=10, pady=10)
    #find_el_button = tkinter.Button(root,text = 'Найти', command=find_spec_el,width = 10)
    #find_el_button.pack(anchor = tkinter.NE, padx = 10, pady = 10)
    root1.mainloop()
