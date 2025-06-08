


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "order_id": _ + 1,
            "customer_id": fake.random_int(min=1, max=1000),
            "order_date": fake.date_time_this_year(),
            "order_status_code": fake.random_element(elements=("Pending", "Shipped", "Delivered", "Cancelled"))
        }
        data.append(record)
    return data
