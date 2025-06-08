


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "project_id": random.randint(1, 1000),
            "outcome_code": fake.lexify(text='??????'),
            "outcome_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
