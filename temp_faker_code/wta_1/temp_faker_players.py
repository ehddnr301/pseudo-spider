


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        player = {
            "player_id": _ + 1,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "hand": random.choice(['left', 'right']),
            "birth_date": fake.date_time_this_year().date(),
            "country_code": fake.country_code()
        }
        data.append(player)
    return data
