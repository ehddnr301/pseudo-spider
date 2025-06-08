


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_ID": fake.random_int(min=1, max=10000),
            "Destruction_Authorised_by_Employee_ID": fake.random_int(min=1, max=1000),
            "Destroyed_by_Employee_ID": fake.random_int(min=1, max=1000),
            "Planned_Destruction_Date": fake.date_time_this_year(),
            "Actual_Destruction_Date": fake.date_time_this_year(),
            "Other_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
