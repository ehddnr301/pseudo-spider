


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": random.uniform(1, 1000),
            "Title": fake.catch_phrase(),
            "Directed_by": fake.name(),
            "Written_by": fake.name(),
            "Original_air_date": fake.date_time_this_year().isoformat(),
            "Production_code": random.uniform(1, 1000),
            "Channel": fake.company()
        }
        data.append(record)
    return data
