


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Tourist_Attraction_ID": random.randint(1, 1000),
            "Feature_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
