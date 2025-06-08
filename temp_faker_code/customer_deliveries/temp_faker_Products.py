



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        product_data = {
            "product_id": _ + 1,
            "product_name": fake.word()[:20],
            "product_price": round(random.uniform(1.0, 1000.0), 4),
            "product_description": fake.text(max_nb_chars=255)
        }
        fake_data.append(product_data)
    return fake_data
