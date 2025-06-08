


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Market_ID": i + 1,
            "Market_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
