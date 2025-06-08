


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "dept_name": fake.unique.word()[:20],
            "building": fake.word()[:15],
            "budget": round(random.uniform(10000, 1000000), 2)
        }
        data.append(record)
    return data
