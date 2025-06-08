


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Campus": random.randint(1, 10),
            "Year": random.randint(2000, 2023),
            "Faculty": round(random.uniform(1.0, 10.0), 2)
        }
        data.append(record)
    return data
