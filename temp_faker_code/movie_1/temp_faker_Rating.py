


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "rID": random.randint(1, 1000),
            "mID": random.randint(1, 1000),
            "stars": random.randint(1, 5),
            "ratingDate": fake.date_time_this_year().date()
        }
        data.append(record)
    return data
