


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": _ + 1,
            "product_category": fake.word()[:15],
            "product_name": fake.text(max_nb_chars=80)[:80]
        }
        data.append(record)
    return data
