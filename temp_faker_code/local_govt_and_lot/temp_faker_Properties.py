


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "property_id": fake.random_int(min=1, max=10000),
            "property_type_code": fake.lexify(text='?????'),
            "property_address": fake.address(),
            "other_details": fake.sentence()
        }
        data.append(record)
    return data
