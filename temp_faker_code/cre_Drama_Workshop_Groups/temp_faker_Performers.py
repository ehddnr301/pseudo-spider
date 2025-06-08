


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Performer_ID": random.randint(1, 1000),
            "Address_ID": random.randint(1, 1000),
            "Customer_Name": fake.name(),
            "Customer_Phone": fake.phone_number(),
            "Customer_Email_Address": fake.email(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
