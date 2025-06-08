


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "SongId": random.randint(1, 1000),
            "Title": fake.sentence(nb_words=3)
        }
        data.append(record)
    return data
