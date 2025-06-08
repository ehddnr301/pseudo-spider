


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "notes_id": random.randint(1, 1000),
            "student_id": random.randint(1, 100),
            "teacher_id": random.randint(1, 100),
            "date_of_notes": fake.date_time_this_year(),
            "text_of_notes": fake.text(max_nb_chars=255),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
