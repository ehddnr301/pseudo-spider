



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Device_ID": random.randint(1, 1000),
            "Device": fake.word(),
            "Carrier": fake.company(),
            "Package_Version": fake.version(),
            "Applications": fake.word(),
            "Software_Platform": fake.word()
        }
        data.append(record)
    return data
