


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "organisation_type": fake.word()[:10],
            "organisation_type_description": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
