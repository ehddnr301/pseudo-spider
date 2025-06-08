



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": _ + 1,
            "product_type_code": fake.word()[:15],
            "daily_hire_cost": round(random.uniform(10.0, 500.0), 4),
            "product_name": fake.word()[:80],
            "product_description": fake.sentence()[:255]
        }
        data.append(record)
    return data
