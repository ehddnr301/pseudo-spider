


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Allergy": fake.word()[:20],
            "AllergyType": fake.word()[:20]
        }
        data.append(record)
    return data
