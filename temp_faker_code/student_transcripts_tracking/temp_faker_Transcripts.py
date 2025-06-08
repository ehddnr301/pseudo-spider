


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "transcript_id": random.randint(1, 1000),
            "transcript_date": fake.date_time_this_year(),
            "other_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
