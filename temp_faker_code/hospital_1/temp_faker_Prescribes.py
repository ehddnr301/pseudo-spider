


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Physician": fake.random_int(min=1, max=100),
            "Patient": fake.random_int(min=1, max=100),
            "Medication": fake.random_int(min=1, max=100),
            "Date": fake.date_time_this_year(),
            "Appointment": fake.random_int(min=1, max=100) ,
            "Dose": fake.word() + " " + fake.random_int(min=1, max=10).__str__()
        }
        data.append(record)
    return data
