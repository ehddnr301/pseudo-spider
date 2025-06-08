


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Attraction_Type_Code": fake.bothify(text='??###??#####'),  # CHAR(15)
            "Attraction_Type_Description": fake.sentence(nb_words=6)  # VARCHAR(255)
        }
        data.append(record)
    return data
