


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 1000),
            "address_id": random.randint(1, 1000),
            "date_from": fake.date_time_this_year(),
            "date_to": fake.date_time_this_year() 
        }
        data.append(record)
    return data
