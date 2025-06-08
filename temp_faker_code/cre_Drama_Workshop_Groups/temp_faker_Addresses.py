


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Address_ID": fake.uuid4(),
            "Line_1": fake.street_address(),
            "Line_2": fake.secondary_address(),
            "City_Town": fake.city(),
            "State_County": fake.state(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
