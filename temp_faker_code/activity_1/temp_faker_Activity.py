


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "actid": _ + 1,
            "activity_name": fake.word()[:25]
        }
        data.append(record)
    return data
