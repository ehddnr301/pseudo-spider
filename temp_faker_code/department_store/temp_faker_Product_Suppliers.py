


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": fake.random_int(min=1, max=1000),
            "supplier_id": fake.random_int(min=1, max=1000),
            "date_supplied_from": fake.date_time_this_year(),
            "date_supplied_to": fake.date_time_this_year(),
            "total_amount_purchased": fake.random_int(min=1, max=10000),
            "total_value_purchased": round(fake.random_number(digits=5) + fake.random.random(), 4)
        }
        data.append(record)
    return data
