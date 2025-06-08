


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "keyword": fake.word(),
            "kid": i + 1
        }
        data.append(record)
    return data
