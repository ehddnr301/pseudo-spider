


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "transaction_id": random.randint(1, 10000),
            "account_id": random.randint(1, 10000),
            "invoice_number": random.randint(1, 10000) ,
            "transaction_type": fake.random_element(elements=("credit", "debit")),
            "transaction_date": fake.date_time_this_year(),
            "transaction_amount": round(random.uniform(1, 10000), 4) ,
            "transaction_comment": fake.sentence() ,
            "other_transaction_details": fake.sentence() 
        }
        data.append(record)
    return data
