


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": fake.random_int(min=1, max=1000),
            "ResID": fake.random_int(min=1, max=100),
            "Time": fake.date_time_this_year(),
            "Spent": round(fake.random_number(digits=3) + fake.random.random(), 2)
        }
        data.append(record)
    return data
