


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Party_ID": i + 1,
            "Party_Details": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
