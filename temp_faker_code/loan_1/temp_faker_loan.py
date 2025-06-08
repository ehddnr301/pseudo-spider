


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "loan_ID": fake.lexify(text='???'),
            "loan_type": fake.random_element(elements=('Personal', 'Home', 'Auto', 'Student')),
            "cust_ID": fake.lexify(text='???'),
            "branch_ID": fake.lexify(text='???'),
            "amount": random.randint(1000, 50000)
        }
        data.append(record)
    return data
