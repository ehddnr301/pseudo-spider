


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "ArtistId": i + 1,
            "Name": fake.name()
        }
        data.append(record)
    return data
