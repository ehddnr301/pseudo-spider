


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Performance_ID": random.uniform(1, 1000),
            "Date": fake.date_time_this_year().isoformat(),
            "Host": fake.name(),
            "Location": fake.city(),
            "Attendance": random.randint(1, 500)
        }
        data.append(record)
    return data
