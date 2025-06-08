


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Service_ID": fake.unique.random_int(min=1, max=1000),
            "Service_Type_Code": fake.lexify(text='?????')
        }
        data.append(record)
    return data
