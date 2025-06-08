


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "attribute_id": fake.random_int(min=1, max=1000),
            "attribute_name": fake.word()[:30],
            "attribute_data_type": random.choice(["string", "integer", "float", "boolean"])
        }
        data.append(record)
    return data
