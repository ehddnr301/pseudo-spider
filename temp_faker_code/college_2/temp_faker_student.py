


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": fake.bothify(text='??###'),
            "name": fake.name(),
            "dept_name": fake.word(),
            "tot_cred": random.randint(0, 999)
        }
        data.append(record)
    return data
