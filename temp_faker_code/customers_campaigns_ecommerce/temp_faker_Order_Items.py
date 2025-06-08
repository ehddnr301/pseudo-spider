


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "item_id": fake.random_int(min=1, max=1000),
            "order_item_status_code": fake.random_element(elements=("Pending", "Shipped", "Delivered")),
            "order_id": fake.random_int(min=1, max=1000),
            "product_id": fake.random_int(min=1, max=1000),
            "item_status_code": fake.random_element(elements=("Available", "Out of Stock")),
            "item_delivered_datetime": fake.date_time_this_year(),
            "item_order_quantity": str(fake.random_int(min=1, max=100))
        }
        data.append(record)
    return data
