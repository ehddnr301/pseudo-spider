


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Event_ID": fake.random_int(min=1, max=1000),
            "Service_ID": fake.random_int(min=1, max=100),
            "Event_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
