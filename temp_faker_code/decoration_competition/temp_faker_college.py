



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "College_ID": random.randint(1, 1000),
            "Name": fake.company(),
            "Leader_Name": fake.name(),
            "College_Location": fake.city()
        }
        data.append(record)
    return data
