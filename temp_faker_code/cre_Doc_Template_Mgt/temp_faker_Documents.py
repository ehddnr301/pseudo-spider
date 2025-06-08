


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_ID": fake.unique.random_int(min=1, max=10000),
            "Template_ID": fake.random_int(min=1, max=100),
            "Document_Name": fake.sentence(nb_words=3),
            "Document_Description": fake.sentence(nb_words=10),
            "Other_Details": fake.sentence(nb_words=5)
        }
        data.append(record)
    return data
