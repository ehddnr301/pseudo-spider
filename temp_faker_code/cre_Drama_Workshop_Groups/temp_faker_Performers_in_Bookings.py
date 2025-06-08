



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Order_ID": random.randint(1, 1000),
            "Performer_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
