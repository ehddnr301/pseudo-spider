


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Id": i + 1,
            "Campus": fake.word(),
            "Location": fake.city(),
            "County": fake.county(),
            "Year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
