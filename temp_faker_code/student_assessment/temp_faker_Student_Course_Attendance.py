


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "student_id": random.randint(1, 1000),
            "course_id": random.randint(1, 100),
            "date_of_attendance": fake.date_time_this_year()
        }
        data.append(record)
    return data
