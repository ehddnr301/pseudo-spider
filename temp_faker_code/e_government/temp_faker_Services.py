


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "service_id": random.randint(1, 1000),
            "service_type_code": fake.lexify(text='???'),
            "service_name": fake.catch_phrase(),
            "service_descriptio": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
