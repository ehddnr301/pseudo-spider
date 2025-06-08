



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "cust_ID": fake.unique.random_int(min=100, max=999),
            "cust_name": fake.name(),
            "acc_type": random.choice(['S', 'C', 'L']),
            "acc_bal": fake.random_int(min=1000, max=100000),
            "no_of_loans": fake.random_int(min=0, max=10),
            "credit_score": fake.random_int(min=300, max=850),
            "branch_ID": fake.random_int(min=1, max=100),
            "state": fake.state()
        }
        data.append(record)
    return data
