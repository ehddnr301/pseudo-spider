


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "characteristic_type_code": fake.bothify(text='??###'),
            "characteristic_type_description": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
