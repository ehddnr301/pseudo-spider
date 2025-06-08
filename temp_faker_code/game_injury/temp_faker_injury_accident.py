


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "game_id": random.randint(1, 100),
            "id": _ + 1,
            "Player": fake.name(),
            "Injury": fake.word(),
            "Number_of_matches": str(random.randint(1, 50)),
            "Source": fake.url()
        }
        data.append(record)
    return data
