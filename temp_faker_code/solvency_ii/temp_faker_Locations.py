


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Location_ID": fake.unique.random_int(min=1, max=1000),
            "Other_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
