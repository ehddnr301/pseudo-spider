


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "skill_id": _ + 1,
            "skill_code": fake.lexify(text='??????'),
            "skill_description": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
