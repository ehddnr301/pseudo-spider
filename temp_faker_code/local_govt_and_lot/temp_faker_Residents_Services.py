


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "resident_id": fake.random_int(min=1, max=1000),
            "service_id": fake.random_int(min=1, max=100),
            "date_moved_in": fake.date_time_this_year(),
            "property_id": fake.random_int(min=1, max=500),
            "date_requested": fake.date_time_this_year(),
            "date_provided": fake.date_time_this_year(),
            "other_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
