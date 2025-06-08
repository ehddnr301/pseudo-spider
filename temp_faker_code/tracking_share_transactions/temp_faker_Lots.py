


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "lot_id": random.randint(1, 1000),
            "investor_id": random.randint(1, 100),
            "lot_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
