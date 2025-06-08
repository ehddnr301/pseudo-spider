


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "enzyme_id": random.randint(1, 100),
            "medicine_id": random.randint(1, 100),
            "interaction_type": fake.word()
        }
        data.append(record)
    return data
