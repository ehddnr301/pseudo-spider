



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "EmployeeID": random.randint(1, 1000),
            "Name": fake.name(),
            "Position": fake.job(),
            "SSN": random.randint(100000000, 999999999)
        }
        data.append(record)
    return data
