


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "document_code": fake.bothify(text='??###'),
            "document_structure_code": fake.bothify(text='??###'),
            "document_type_code": fake.bothify(text='??###'),
            "access_count": random.randint(0, 100),
            "document_name": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
