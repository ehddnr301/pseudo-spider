


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Patient": fake.random_int(min=1, max=1000),
            "Procedures": fake.random_int(min=1, max=100),
            "Stay": fake.random_int(min=1, max=30),
            "DateUndergoes": fake.date_time_this_year(),
            "Physician": fake.random_int(min=1, max=500),
            "AssistingNurse": fake.random_int(min=1, max=1000) 
        }
        data.append(record)
    return data
