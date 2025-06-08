



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Store_ID": fake.random_int(min=1, max=1000),
            "District_ID": fake.random_int(min=1, max=100)
        }
        data.append(record)
    return data
