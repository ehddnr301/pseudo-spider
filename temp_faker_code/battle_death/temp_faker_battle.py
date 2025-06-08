


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.name(),
            "date": fake.date_time_this_year().isoformat(),
            "bulgarian_commander": fake.name(),
            "latin_commander": fake.name(),
            "result": random.choice(["Victory", "Defeat", "Draw"])
        }
        data.append(record)
    return data
