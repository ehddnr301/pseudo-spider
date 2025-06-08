


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": fake.random_int(min=1, max=1000),
            "address_id": fake.random_int(min=1, max=1000),
            "date_address_from": fake.date_time_this_year(),
            "address_type": fake.random_element(elements=("home", "work", "billing")),
            "date_address_to": fake.date_time_this_year() 
        }
        data.append(record)
    return data
