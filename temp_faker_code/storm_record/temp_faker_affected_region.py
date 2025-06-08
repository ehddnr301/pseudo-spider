


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Region_id": fake.random_int(min=1, max=1000),
            "Storm_ID": fake.random_int(min=1, max=100),
            "Number_city_affected": round(fake.random_number(digits=2) * random.uniform(0.1, 1.0), 2)
        }
        data.append(record)
    return data
