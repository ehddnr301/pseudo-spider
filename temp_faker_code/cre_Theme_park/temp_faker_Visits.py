


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Visit_ID": _ + 1,
            "Tourist_Attraction_ID": fake.random_int(min=1, max=100),
            "Tourist_ID": fake.random_int(min=1, max=1000),
            "Visit_Date": fake.date_time_this_year(),
            "Visit_Details": fake.text(max_nb_chars=40)[:40]
        }
        data.append(record)
    return data
