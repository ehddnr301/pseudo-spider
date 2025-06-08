


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "grant_id": _ + 1,
            "organisation_id": random.randint(1, 100),
            "grant_amount": round(random.uniform(1000, 100000), 4),
            "grant_start_date": fake.date_time_this_year(),
            "grant_end_date": fake.date_time_this_year(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
