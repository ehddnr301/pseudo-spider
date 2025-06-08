


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Location_ID": i + 1,
            "Location_Name": fake.company(),
            "Address": fake.address(),
            "Other_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
