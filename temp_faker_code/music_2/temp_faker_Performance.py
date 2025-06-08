


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "SongId": random.randint(1, 1000),
            "Bandmate": random.randint(1, 10),
            "StagePosition": fake.random_element(elements=("Lead", "Rhythm", "Bass", "Drums", "Vocals"))
        }
        data.append(record)
    return data
