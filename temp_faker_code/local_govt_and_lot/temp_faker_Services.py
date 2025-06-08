


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "service_id": fake.random_int(min=1, max=1000),
            "organization_id": fake.random_int(min=1, max=100),
            "service_type_code": fake.lexify(text='?????'),
            "service_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
