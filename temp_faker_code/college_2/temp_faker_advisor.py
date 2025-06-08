



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "s_ID": fake.bothify(text='??###'),
            "i_ID": fake.bothify(text='??###')
        }
        data.append(record)
    return data
