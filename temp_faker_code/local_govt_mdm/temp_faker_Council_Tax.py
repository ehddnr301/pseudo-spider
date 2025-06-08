

import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "council_tax_id": fake.random_int(min=1, max=10000),
            "cmi_cross_ref_id": fake.random_int(min=1, max=10000)
        }
        data.append(record)
    return data
