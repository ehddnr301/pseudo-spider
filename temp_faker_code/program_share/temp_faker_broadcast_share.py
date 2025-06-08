


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Channel_ID": fake.random_int(min=1, max=100),
            "Program_ID": fake.random_int(min=1, max=100),
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Share_in_percent": round(fake.random.uniform(0, 100), 2)
        }
        data.append(record)
    return data
