



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "purchase_transaction_id": random.randint(1, 10000),
            "purchase_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
