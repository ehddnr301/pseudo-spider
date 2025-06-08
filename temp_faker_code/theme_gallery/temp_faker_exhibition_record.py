


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Exhibition_ID": fake.unique.random_int(min=1, max=1000),
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Attendance": fake.random_int(min=0, max=10000)
        }
        data.append(record)
    return data
