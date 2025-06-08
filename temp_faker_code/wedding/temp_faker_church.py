


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Church_ID": _ + 1,
            "Name": fake.company(),
            "Organized_by": fake.name(),
            "Open_Date": int(fake.date_time_this_year().timestamp()),
            "Continuation_of": fake.company_suffix()
        }
        data.append(record)
    return data
