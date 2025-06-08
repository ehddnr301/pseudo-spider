


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Graphics_mode": random.uniform(0, 10),
            "Char_cells": fake.word(),
            "Pixels": fake.word(),
            "Hardware_colours": random.uniform(0, 10),
            "used_kb": random.uniform(0, 100),
            "map": fake.word(),
            "Type": fake.word()
        }
        data.append(record)
    return data
