



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Employee_ID": random.randint(1, 1000),
            "Name": fake.name(),
            "Age": random.randint(18, 65),
            "City": fake.city()
        }
        data.append(record)
    return data
