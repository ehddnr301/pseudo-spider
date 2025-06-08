



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "sales_transaction_id": random.randint(1, 10000),
            "sales_details": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
