


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "uid": _ + 1,
            "Airline": fake.company(),
            "Abbreviation": fake.word().upper(),
            "Country": fake.country()
        }
        data.append(record)
    return data
