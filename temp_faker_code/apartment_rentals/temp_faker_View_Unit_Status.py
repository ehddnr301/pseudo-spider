


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "apt_id": random.randint(1, 100),
            "apt_booking_id": random.randint(1, 100),
            "status_date": fake.date_time_this_year(),
            "available_yn": random.choice([0, 1])
        }
        data.append(record)
    return data
