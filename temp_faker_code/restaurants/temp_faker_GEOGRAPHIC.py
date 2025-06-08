


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CITY_NAME": fake.city(),
            "COUNTY": fake.county(),
            "REGION": fake.state()
        }
        data.append(record)
    return data
