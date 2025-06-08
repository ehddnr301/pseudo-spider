


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Physician": fake.random_int(min=1, max=100),
            "Treatment": fake.random_int(min=1, max=100),
            "CertificationDate": fake.date_time_this_year(),
            "CertificationExpires": fake.date_time_this_year()
        }
        data.append(record)
    return data
