


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Store_ID": fake.uuid4(),
            "Address_ID": fake.random_int(min=1, max=1000),
            "Marketing_Region_Code": fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "Store_Name": fake.company(),
            "Store_Phone": fake.phone_number(),
            "Store_Email_Address": fake.email(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
