


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Election_ID": _ + 1,
            "Counties_Represented": fake.city(),
            "District": random.randint(1, 100),
            "Delegate": fake.name(),
            "Party": random.randint(1, 5),
            "First_Elected": fake.date_time_this_year().timestamp(),
            "Committee": fake.word()
        }
        data.append(record)
    return data
