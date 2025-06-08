


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "SongId": fake.random_int(min=1, max=1000),
            "Bandmate": fake.random_int(min=1, max=10),
            "Type": fake.word()
        }
        data.append(record)
    return data
