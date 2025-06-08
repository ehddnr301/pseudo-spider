


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": _ + 1,
            "LName": fake.last_name()[:12],
            "Fname": fake.first_name()[:12],
            "Age": random.randint(18, 25),
            "Sex": random.choice(['M', 'F']),
            "Major": random.randint(1, 10),
            "Advisor": random.randint(1, 10),
            "city_code": fake.city()[:3].upper()
        }
        data.append(record)
    return data
