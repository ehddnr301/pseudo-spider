


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Region_id": random.randint(1, 1000),
            "Region_code": fake.state_abbr(),
            "Region_name": fake.region()
        }
        data.append(record)
    return data
