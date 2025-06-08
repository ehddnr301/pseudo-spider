



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "custid": fake.random_int(min=1, max=9999999999),
            "balance": round(random.uniform(0, 10000), 2)
        }
        data.append(record)
    return data
