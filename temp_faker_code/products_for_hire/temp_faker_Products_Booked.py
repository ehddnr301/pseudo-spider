



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "booking_id": fake.unique.random_int(min=1, max=10000),
            "product_id": fake.unique.random_int(min=1, max=10000),
            "returned_yn": random.choice(['Y', 'N']),
            "returned_late_yn": random.choice(['Y', 'N']),
            "booked_count": fake.random_int(min=1, max=100),
            "booked_amount": round(fake.random_number(digits=5) / 100, 2)
        }
        data.append(record)
    return data
