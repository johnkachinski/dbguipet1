class Order:
    def __init__(self,product_name,quantity,customer_id):
        self.product_name = product_name
        self.quantity = quantity
        self.customer_id = customer_id


class Ordershow:
    def __init__(self,order_id,order_name,barcode,quantity,customer_id):
        self.order_id = order_id
        self.order_name = order_name
        self.barcode = barcode
        self.quantity = quantity
        self.customer_id = customer_id