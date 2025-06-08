


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "year": fake.year(),
            "league_id": fake.word(),
            "team_id": fake.word(),
            "franchise_id": fake.word(),
            "div_id": fake.word(),
            "rank": random.randint(1, 30),
            "g": random.randint(1, 162),
            "ghome": random.uniform(0, 1),
            "w": random.randint(0, 162),
            "l": random.randint(0, 162),
            "div_win": fake.word(),
            "wc_win": fake.word(),
            "lg_win": fake.word(),
            "ws_win": fake.word(),
            "r": random.randint(0, 1000),
            "ab": random.randint(0, 6000),
            "h": random.randint(0, 2000),
            "double": random.randint(0, 500),
            "triple": random.randint(0, 100),
            "hr": random.randint(0, 300),
            "bb": random.randint
