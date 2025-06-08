


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "head_ID": _ + 1,
            "name": fake.name(),
            "born_state": fake.state(),
            "age": round(random.uniform(18, 80), 1)
        }
        data.append(record)
    return data
