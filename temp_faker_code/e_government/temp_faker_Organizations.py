


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "organization_id": random.randint(1, 1000),
            "date_formed": fake.date_time_this_year(),
            "organization_name": fake.company(),
            "uk_vat_number": fake.bothify(text='??##??######')
        }
        data.append(record)
    return data
