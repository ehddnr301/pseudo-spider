


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Client_ID": _ + 1,
            "Address_ID": random.randint(1, 100),
            "Customer_Email_Address": fake.email(),
            "Customer_Name": fake.name(),
            "Customer_Phone": fake.phone_number(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
