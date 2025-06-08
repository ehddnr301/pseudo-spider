



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": random.randint(1, 1000),
            "Member_Name": fake.name(),
            "Party_ID": fake.word(),
            "In_office": fake.word()
        }
        data.append(record)
    return data
