



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "InvoiceLineId": fake.unique.random_int(min=1, max=10000),
            "InvoiceId": fake.random_int(min=1, max=1000),
            "TrackId": fake.random_int(min=1, max=1000),
            "UnitPrice": round(random.uniform(1.00, 100.00), 2),
            "Quantity": fake.random_int(min=1, max=10)
        }
        data.append(record)
    return data
