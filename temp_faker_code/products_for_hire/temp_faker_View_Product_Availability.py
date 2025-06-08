


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": fake.random_int(min=1, max=1000),
            "booking_id": fake.random_int(min=1, max=1000),
            "status_date": fake.date_time_this_year(),
            "available_yn": fake.random_element(elements=('Y', 'N'))
        }
        data.append(record)
    return data
