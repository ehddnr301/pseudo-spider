


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "order_id": random.randint(1, 1000),
            "customer_id": random.randint(1, 100),
            "date_order_placed": fake.date_time_this_year(),
            "order_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
