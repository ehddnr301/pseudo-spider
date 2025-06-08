


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        order_id = random.randint(1, 1000)
        customer_id = random.randint(1, 100)
        order_status_code = fake.random_element(elements=('Pending', 'Shipped', 'Delivered', 'Cancelled'))
        shipping_method_code = fake.random_element(elements=('Standard', 'Express', 'Overnight'))
        order_placed_datetime = fake.date_time_this_year()
        order_delivered_datetime = fake.date_time_this_year() 
        order_shipping_charges = fake.random_int(min=0, max=100)
        
        data.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "order_status_code": order_status_code,
            "shipping_method_code": shipping_method_code,
            "order_placed_datetime": order_placed_datetime,
            "order_delivered_datetime": order_delivered_datetime,
            "order_shipping_charges": str(order_shipping_charges)
        })
    return data
