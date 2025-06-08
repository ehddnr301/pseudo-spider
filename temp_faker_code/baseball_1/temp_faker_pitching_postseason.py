


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "player_id": fake.uuid4(),
            "year": fake.year(),
            "round": fake.random_element(elements=("ALDS", "ALCS", "NLDS", "NLCS", "WS")),
            "team_id": fake.random_element(elements=("NYY", "BOS", "LAD", "CHC", "HOU")),
            "league_id": fake.random_element(elements=("AL", "NL")),
            "w": fake.random_int(min=0, max=5),
            "l": fake.random_int(min=0, max=5),
            "g": fake.random_int(min=1, max=7),
            "gs": fake.random_int(min=0, max=5),
            "cg": fake.random_int(min=0, max=5),
            "sho": fake.random_int(min=0, max=5),
            "sv": fake.random_int(min=0, max=5),
            "ipouts": fake.random_int(min=1, max=30),
            "h": fake.random_int
