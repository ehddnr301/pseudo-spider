


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Teacher_ID": _ + 1,
            "Name": fake.name(),
            "Age": str(random.randint(25, 60)),
            "Hometown": fake.city()
        }
        data.append(record)
    return data
