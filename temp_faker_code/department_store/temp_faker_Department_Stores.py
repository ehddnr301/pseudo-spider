



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "dept_store_id": random.randint(1, 1000),
            "dept_store_chain_id": random.randint(1, 100),
            "store_name": fake.company(),
            "store_address": fake.address(),
            "store_phone": fake.phone_number(),
            "store_email": fake.email()
        }
        data.append(record)
    return data
