



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "u_id": random.randint(1, 1000),  # INTEGER 타입
            "name": fake.name()  # varchar(128) 타입
        }
        data.append(record)
    return data
