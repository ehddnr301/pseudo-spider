



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_ID": fake.random_int(min=1, max=1000),
            "Driver_ID": fake.random_int(min=1, max=1000),
            "Years_Working": fake.random_int(min=1, max=30),
            "If_full_time": fake.boolean()
        }
        data.append(record)
    return data
