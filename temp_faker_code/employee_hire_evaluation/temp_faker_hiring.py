


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Shop_ID": random.randint(1, 100),
            "Employee_ID": fake.unique.random_int(min=1, max=1000),
            "Start_from": fake.date_time_this_year().isoformat(),
            "Is_full_time": fake.boolean()
        }
        data.append(record)
    return data
