


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Editor_ID": fake.random_int(min=1, max=1000),
            "Journal_ID": fake.random_int(min=1, max=1000),
            "Work_Type": fake.word()
        }
        data.append(record)
    return data
