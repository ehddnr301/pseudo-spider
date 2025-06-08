


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "premise_id": _ + 1,
            "premises_type": fake.word()[:15],
            "premise_details": fake.sentence()[:255]
        }
        data.append(record)
    return data
