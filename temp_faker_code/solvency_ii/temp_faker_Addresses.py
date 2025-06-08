



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Address_ID": i + 1,
            "address_details": fake.address()
        }
        data.append(record)
    return data
