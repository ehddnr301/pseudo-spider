


from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": fake.random_int(min=1, max=1000),
            "CID": fake.bothify(text='???###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            "Grade": random.choice(['A', 'B', 'C', 'D', 'F'])
        }
        data.append(record)
    return data
