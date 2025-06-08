


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "County_Id": _ + 1,
            "County_name": fake.city(),
            "Population": random.uniform(1000, 100000),
            "Zip_code": fake.zipcode()
        }
        data.append(record)
    return data
