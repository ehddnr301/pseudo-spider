


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Scientist": fake.random_int(min=1, max=1000),
            "Project": fake.bothify(text='???#')
        }
        data.append(record)
    return data
