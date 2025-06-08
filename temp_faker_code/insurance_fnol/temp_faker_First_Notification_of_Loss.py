



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "FNOL_ID": fake.random_int(min=1, max=1000),
            "Customer_ID": fake.random_int(min=1, max=1000),
            "Policy_ID": fake.random_int(min=1, max=1000),
            "Service_ID": fake.random_int(min=1, max=1000)
        }
        data.append(record)
    return data
