


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 1000),
            "customer_name": fake.name(),
            "customer_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
