


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "organisation_id": random.randint(1, 1000),
            "organisation_type": fake.word()[:10],
            "organisation_details": fake.sentence()[:255]
        }
        data.append(record)
    return data
