



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": _ + 1,
            "parent_product_id": random.choice([None, random.randint(1, 100)]),
            "product_category_code": fake.word()[:20],
            "date_product_first_available": fake.date_time_this_year(),
            "date_product_discontinued": fake.date_time_this_year(),
            "product_name": fake.word()[:80],
            "product_description": fake.sentence()[:255],
            "product_price": round(random.uniform(1, 1000), 4)
        }
        data.append(record)
    return data
