


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Course_ID": random.randint(1, 1000),
            "Staring_Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Course": fake.word()
        }
        data.append(record)
    return data
