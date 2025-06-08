


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.company(),
            "market_share": round(random.uniform(0, 100), 2)
        }
        data.append(record)
    return data
