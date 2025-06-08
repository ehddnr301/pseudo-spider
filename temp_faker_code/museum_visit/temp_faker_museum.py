


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Museum_ID": fake.unique.random_int(min=1, max=1000),
            "Name": fake.company(),
            "Num_of_Staff": fake.random_int(min=1, max=100),
            "Open_Year": str(fake.date_time_this_year().year)
        }
        data.append(record)
    return data
