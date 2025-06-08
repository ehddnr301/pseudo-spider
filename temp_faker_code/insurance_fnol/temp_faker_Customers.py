



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Customer_ID": random.randint(1, 1000),
            "Customer_name": fake.name()
        }
        data.append(record)
    return data
