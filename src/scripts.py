from base import sessionlocal,text


def fetchall_orders():
    rslt = ''
    with sessionlocal() as session:
        key = '`Order ID`'
        instance = session.execute(text(f'SELECT * FROM orders ORDER BY {key}'))
        rslt = instance.fetchall()
    return rslt

def fetchall_goods():
    rslt = ''
    with sessionlocal() as session:
        key = '`Barcode`'
        instance = session.execute(text(f'SELECT * FROM goods ORDER BY {key}'))
        rslt = instance.fetchall()
    return rslt

def fetchall_customers():
    rslt = ''
    with sessionlocal() as session:
        key = '`Customer ID`'
        instance = session.execute(text(f'SELECT * FROM customers ORDER BY {key}'))
        rslt = instance.fetchall()
    return rslt

def add_new_order(query):
    barcode = ''
    with sessionlocal() as session:
        barcode = session.execute(text(f'SELECT Barcode FROM goods WHERE `Product Name` = {query.product_name}'))
        barcode = barcode.first()
        barcode = barcode[0]
        date = session.execute(text('SELECT CURRENT_DATE'))
        date = date.first()
        date = date[0]
        date = f'"{date}"'
        session.execute(text(f'INSERT INTO orders (`Order Date`,Barcode,Quantity,`Customer ID`) VALUES ({date},{barcode},{query.quantity},{query.customer_id})'))
        session.commit()

def get_customer_id(customer_id):
    with sessionlocal() as session:
        f = session.execute(text(f'SELECT * FROM orders WHERE `Customer ID`={int(customer_id)}'))
        f = f.fetchall()
    return f