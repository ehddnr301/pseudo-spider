


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_ID": fake.random_int(min=1, max=1000),
            "Document_Type_Code": fake.lexify(text='???'),
            "Project_ID": fake.random_int(min=1, max=100),
            "Document_Date": fake.date_time_this_year(),
            "Document_Name": fake.sentence(nb_words=3),
            "Document_Description": fake.sentence(nb_words=6),
            "Other_Details": fake.sentence(nb_words=4)
        }
        data.append(record)
    return data
