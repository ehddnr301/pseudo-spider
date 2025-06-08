


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "dept_store_chain_id": fake.random_int(min=1, max=1000),
            "dept_store_chain_name": fake.company()[:80]
        }
        data.append(record)
    return data
