



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": None,  # Primary key, can be None
            "invoice_id": random.randint(1, 1000),  # Assuming invoice_id is between 1 and 1000
            "track_id": random.randint(1, 1000),  # Assuming track_id is between 1 and 1000
            "unit_price": round(random.uniform(1.0, 100.0), 2),  # Random price between 1.0 and 100.0
            "quantity": random.randint(1, 10)  # Random quantity between 1 and 10
        }
        data.append(record)
    return data
