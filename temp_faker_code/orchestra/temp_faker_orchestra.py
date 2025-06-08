


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Orchestra_ID": fake.unique.random_int(min=1, max=1000),
            "Orchestra": fake.company(),
            "Conductor_ID": fake.random_int(min=1, max=100),
            "Record_Company": fake.company(),
            "Year_of_Founded": fake.year(),
            "Major_Record_Format": fake.random_element(elements=("CD", "Vinyl", "Digital"))
        }
        data.append(record)
    return data
