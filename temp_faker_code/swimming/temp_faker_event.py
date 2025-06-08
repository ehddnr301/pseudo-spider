


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "Name": fake.name(),
            "Stadium_ID": random.randint(1, 100),
            "Year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
