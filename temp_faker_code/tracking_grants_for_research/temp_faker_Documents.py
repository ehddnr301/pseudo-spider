


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "document_id": random.randint(1, 1000),
            "document_type_code": fake.lexify(text='??????'),
            "grant_id": random.randint(1, 100),
            "sent_date": fake.date_time_this_year(),
            "response_received_date": fake.date_time_this_year(),
            "other_details": fake.text(max_nb_chars=255)
        }
        fake_data.append(record)
    return fake_data
