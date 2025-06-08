


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "document_id": fake.random_int(min=1, max=1000),
            "mailed_to_address_id": fake.random_int(min=1, max=1000),
            "mailing_date": fake.date_time_this_year()
        }
        data.append(record)
    return data
