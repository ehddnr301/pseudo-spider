


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Statement_ID": i + 1,
            "Statement_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
