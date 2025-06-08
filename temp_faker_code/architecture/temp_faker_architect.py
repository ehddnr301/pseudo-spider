


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": fake.uuid4(),
            "name": fake.name(),
            "nationality": fake.country(),
            "gender": random.choice(["Male", "Female"])
        }
        data.append(record)
    return data
