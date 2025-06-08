


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StayID": _ + 1,
            "Patient": random.randint(1, 100),
            "Room": random.randint(1, 50),
            "StayStart": fake.date_time_this_year(),
            "StayEnd": fake.date_time_this_year()
        }
        data.append(record)
    return data
