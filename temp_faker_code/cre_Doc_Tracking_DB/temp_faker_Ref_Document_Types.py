


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_Type_Code": fake.bothify(text='???-######'),
            "Document_Type_Name": fake.sentence(nb_words=3),
            "Document_Type_Description": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
