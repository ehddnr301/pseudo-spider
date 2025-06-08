


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "a_id": fake.unique.random_int(min=1, max=1000),
            "u_id": fake.unique.random_int(min=1, max=1000),
            "i_id": fake.unique.random_int(min=1, max=1000),
            "rating": random.randint(1, 5),
            "rank": random.randint(1, 10)
        }
        data.append(record)
    return data
