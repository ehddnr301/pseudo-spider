


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "detention_id": random.randint(1, 1000),
            "detention_type_code": fake.word()[:10],
            "teacher_id": random.randint(1, 100),
            "datetime_detention_start": fake.date_time_this_year(),
            "datetime_detention_end": fake.date_time_this_year(),
            "detention_summary": fake.sentence()[:255],
            "other_details": fake.sentence()[:255]
        }
        data.append(record)
    return data
