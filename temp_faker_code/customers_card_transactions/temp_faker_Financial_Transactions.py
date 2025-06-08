



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "transaction_id": fake.random_int(min=1, max=10000),
            "previous_transaction_id": fake.random_int(min=1, max=10000) ,
            "account_id": fake.random_int(min=1, max=10000),
            "card_id": fake.random_int(min=1, max=10000),
            "transaction_type": fake.random_element(elements=("debit", "credit", "transfer")),
            "transaction_date": fake.date_time_this_year(),
            "transaction_amount": round(fake.random_number(digits=5) + fake.random.random(), 2),
            "transaction_comment": fake.sentence(),
            "other_transaction_details": fake.sentence()
        }
        data.append(record)
    return data
