



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "SSN": fake.random_int(min=100000000, max=999999999),
            "Name": fake.name(),
            "Address": fake.address().replace("\n", ", "),
            "Phone": fake.phone_number(),
            "InsuranceID": fake.random_int(min=100000, max=999999),
            "PCP": fake.random_int(min=1, max=100)
        }
        data.append(record)
    return data
