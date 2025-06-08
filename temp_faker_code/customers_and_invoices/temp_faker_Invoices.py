


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "invoice_number": random.randint(1, 1000),
            "order_id": random.randint(1, 1000),
            "invoice_date": fake.date_time_this_year()
        }
        data.append(record)
    return data
