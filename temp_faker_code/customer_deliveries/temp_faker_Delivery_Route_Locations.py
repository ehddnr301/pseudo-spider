


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "location_code": fake.bothify(text='??###'),
            "route_id": random.randint(1, 100),
            "location_address_id": random.randint(1, 1000),
            "location_name": fake.company()  # or fake.street_name() depending on your needs
        }
        data.append(record)
    return data
