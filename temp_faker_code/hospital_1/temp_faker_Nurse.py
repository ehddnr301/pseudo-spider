


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "EmployeeID": fake.unique.random_int(min=1, max=1000),
            "Name": fake.name(),
            "Position": fake.job(),
            "Registered": fake.boolean(),
            "SSN": fake.unique.random_int(min=100000000, max=999999999)
        }
        data.append(record)
    return data
