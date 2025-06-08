



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": _ + 1,
            "color_code": fake.color_name(),
            "product_category_code": fake.word(),
            "product_name": fake.word() + " " + fake.word(),
            "typical_buying_price": str(round(random.uniform(1, 100), 2)),
            "typical_selling_price": str(round(random.uniform(1, 100), 2)),
            "product_description": fake.sentence(),
            "other_product_details": fake.sentence()
        }
        data.append(record)
    return data
