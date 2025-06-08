


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ranking_date": fake.date_time_this_year().date(),
            "ranking": random.randint(1, 100),
            "player_id": random.randint(1, 1000),
            "ranking_points": random.randint(0, 5000),
            "tours": random.randint(1, 50)
        }
        data.append(record)
    return data
