



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": fake.random_int(min=1, max=1000),
            "Performance_ID": fake.random_int(min=1, max=100),
            "Num_of_Pieces": fake.random_int(min=1, max=50)
        }
        data.append(record)
    return data
