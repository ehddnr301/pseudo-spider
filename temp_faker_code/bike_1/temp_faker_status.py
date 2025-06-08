


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "station_id": fake.random_int(min=1, max=100),
            "bikes_available": fake.random_int(min=0, max=20),
            "docks_available": fake.random_int(min=0, max=20),
            "time": fake.date_time_this_year().isoformat()
        }
        data.append(record)
    return data
