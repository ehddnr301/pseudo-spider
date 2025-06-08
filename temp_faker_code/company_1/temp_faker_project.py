


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Pname": fake.word(),
            "Pnumber": random.randint(1, 1000),
            "Plocation": fake.city(),
            "Dnum": random.randint(1, 10)
        }
        data.append(record)
    return data
