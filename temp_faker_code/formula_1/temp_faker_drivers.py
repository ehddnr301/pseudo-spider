


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "driverId": _ + 1,
            "driverRef": fake.word(),
            "number": fake.random_int(min=1, max=99),
            "code": fake.word(),
            "forename": fake.first_name(),
            "surname": fake.last_name(),
            "dob": fake.date_time_this_year().strftime('%Y-%m-%d'),
            "nationality": fake.country(),
            "url": fake.url()
        }
        data.append(record)
    return data
