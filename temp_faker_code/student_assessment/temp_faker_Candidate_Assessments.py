


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "candidate_id": fake.random_int(min=1, max=1000),
            "qualification": fake.random_element(elements=("Bachelor", "Master", "PhD")),
            "assessment_date": fake.date_time_this_year(),
            "asessment_outcome_code": fake.random_element(elements=("Pass", "Fail", "Pending"))
        }
        data.append(record)
    return data
