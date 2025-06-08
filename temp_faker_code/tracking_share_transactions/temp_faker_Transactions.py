


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "transaction_id": _ + 1,
            "investor_id": fake.random_int(min=1, max=1000),
            "transaction_type_code": fake.random_element(elements=("BUY", "SELL")),
            "date_of_transaction": fake.date_time_this_year(),
            "amount_of_transaction": round(fake.random_number(digits=10), 4),
            "share_count": str(fake.random_int(min=1, max=100)),
            "other_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
