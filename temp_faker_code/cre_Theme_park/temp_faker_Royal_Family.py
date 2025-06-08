


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Royal_Family_ID": fake.unique.random_int(min=1, max=1000),
            "Royal_Family_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
