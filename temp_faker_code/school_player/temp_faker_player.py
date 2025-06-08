


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Player_ID": _ + 1,
            "Player": fake.name(),
            "Team": fake.word(),
            "Age": random.randint(18, 40),
            "Position": fake.word(),
            "School_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
