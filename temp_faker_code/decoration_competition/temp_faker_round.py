


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Round_ID": fake.random_int(min=1, max=1000),
            "Member_ID": fake.random_int(min=1, max=1000),
            "Decoration_Theme": fake.word(),
            "Rank_in_Round": fake.random_int(min=1, max=10)
        }
        data.append(record)
    return data
