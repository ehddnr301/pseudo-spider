



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "Party_ID": fake.random_int(min=1, max=1000),
            "Host_ID": fake.random_int(min=1, max=1000),
            "Is_Main_in_Charge": fake.boolean()
        }
        data.append(record)
    return data
