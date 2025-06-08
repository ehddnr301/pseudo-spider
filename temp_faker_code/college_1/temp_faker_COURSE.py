


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CRS_CODE": fake.bothify(text='??###'),
            "DEPT_CODE": fake.bothify(text='??'),
            "CRS_DESCRIPTION": fake.sentence(nb_words=6),
            "CRS_CREDIT": round(random.uniform(1.0, 5.0), 2)
        }
        data.append(record)
    return data
