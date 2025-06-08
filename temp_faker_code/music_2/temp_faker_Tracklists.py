


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "AlbumId": fake.random_int(min=1, max=1000),
            "Position": fake.random_int(min=1, max=20),
            "SongId": fake.random_int(min=1, max=5000)
        }
        data.append(record)
    return data
