



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "catalog_entry_id": _ + 1,
            "catalog_level_number": random.randint(1, 10),
            "parent_entry_id": random.choice([None, random.randint(1, 100)]),
            "previous_entry_id": random.choice([None, random.randint(1, 100)]),
            "next_entry_id": random.choice([None, random.randint(1, 100)]),
            "catalog_entry_name": fake.word()[:80],
            "product_stock_number": fake.word()[:50],
            "price_in_dollars": round(random.uniform(1, 1000), 2),
            "price_in_euros": round(random.uniform(1, 1000), 2),
            "price_in_pounds": round(random.uniform(1, 1000), 2),
            "capacity": fake.word()[:20],
            "length": fake.word()[:20],
            "height": fake.word()[:20],
            "width": fake.word()[:20]
        }
        data.append(record)
