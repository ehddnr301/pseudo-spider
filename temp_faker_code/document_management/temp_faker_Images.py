


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "image_id": random.randint(1, 1000),
            "image_alt_text": fake.sentence(nb_words=6),
            "image_name": fake.word(),
            "image_url": fake.image_url()
        }
        data.append(record)
    return data
