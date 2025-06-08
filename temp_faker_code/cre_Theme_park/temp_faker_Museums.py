


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Museum_ID": i + 1,
            "Museum_Details": fake.sentence(nb_words=6)  # VARCHAR(255)
        }
        data.append(record)
    return data
