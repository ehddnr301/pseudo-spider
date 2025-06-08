


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ClubID": random.randint(1, 1000),
            "ClubName": fake.word()[:40],
            "ClubDesc": fake.text(max_nb_chars=1024),
            "ClubLocation": fake.word()[:40]
        }
        data.append(record)
    return data
