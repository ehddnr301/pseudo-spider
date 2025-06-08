


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Finance_ID": fake.random_int(min=1, max=10000),
            "Other_Details": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
