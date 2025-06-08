


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "student_id": fake.random_int(min=1, max=1000),
            "course_id": fake.random_int(min=1, max=100),
            "registration_date": fake.date_time_this_year()
        }
        data.append(record)
    return data
