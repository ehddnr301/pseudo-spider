


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "store_id": random.randint(1, 255),
            "manager_staff_id": random.randint(1, 255),
            "address_id": random.randint(1, 65535),
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
