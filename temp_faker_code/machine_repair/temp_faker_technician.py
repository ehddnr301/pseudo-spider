


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "technician_id": fake.random_int(min=1, max=1000),
            "Name": fake.name(),
            "Team": fake.word(),
            "Starting_Year": fake.date_time_this_year().year,
            "Age": fake.random_int(min=20, max=60)
        }
        data.append(record)
    return data
