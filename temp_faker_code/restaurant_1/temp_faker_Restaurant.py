


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "ResID": i + 1,
            "ResName": fake.company(),
            "Address": fake.address().replace("\n", ", "),
            "Rating": random.randint(1, 5)
        }
        data.append(record)
    return data
