


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "language_id": random.randint(1, 255),  # TINYINT UNSIGNED
            "name": fake.word()[:20],  # CHAR(20)
            "last_update": fake.date_time_this_year()  # TIMESTAMP
        }
        data.append(record)
    return data
