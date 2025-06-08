


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Station_ID": fake.random_int(min=1, max=1000),
            "Company_ID": fake.random_int(min=1, max=100),
            "Rank_of_the_Year": fake.random_int(min=1, max=10)
        }
        data.append(record)
    return data
