


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "custid": fake.random_int(min=1, max=1000000),
            "balance": round(fake.random_number(digits=5) + fake.random.random(), 2)
        }
        data.append(record)
    return data
