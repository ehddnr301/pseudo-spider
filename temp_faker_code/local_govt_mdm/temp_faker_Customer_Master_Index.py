


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "master_customer_id": fake.unique.random_int(min=1, max=10000),
            "cmi_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
