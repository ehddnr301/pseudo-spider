


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "incident_id": _ + 1,
            "incident_type_code": fake.word()[:10],
            "student_id": random.randint(1, 1000),
            "date_incident_start": fake.date_time_this_year(),
            "date_incident_end": fake.date_time_this_year(),
            "incident_summary": fake.sentence(),
            "recommendations": fake.sentence(),
            "other_details": fake.sentence()
        }
        data.append(record)
    return data
