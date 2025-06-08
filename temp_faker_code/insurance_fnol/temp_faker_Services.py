


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Service_ID": _ + 1,
            "Service_name": fake.word()[:40]
        }
        data.append(record)
    return data
