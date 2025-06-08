


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "GameID": i + 1,
            "GName": fake.word()[:40],
            "GType": fake.word()[:40]
        }
        data.append(record)
    return data
