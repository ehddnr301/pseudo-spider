



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "branch_ID": random.randint(1, 1000),
            "bname": fake.company()[:20],
            "no_of_customers": random.randint(1, 1000),
            "city": fake.city()[:10],
            "state": fake.state()[:20]
        }
        data.append(record)
    return data
