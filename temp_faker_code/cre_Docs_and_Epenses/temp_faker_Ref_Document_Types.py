


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_Type_Code": fake.bothify(text='???-######'),
            "Document_Type_Name": fake.catch_phrase(),
            "Document_Type_Description": fake.sentence()
        }
        data.append(record)
    return data
