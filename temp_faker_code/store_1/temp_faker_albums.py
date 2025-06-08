


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "title": fake.sentence(nb_words=3),  # VARCHAR(160)
            "artist_id": random.randint(1, 100)  # INTEGER
        }
        data.append(record)
    return data
