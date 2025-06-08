



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        order_item = {
            "order_item_id": fake.unique.random_int(min=1, max=1000),
            "order_id": fake.random_int(min=1, max=100),
            "product_id": fake.random_int(min=1, max=100),
            "product_quantity": str(fake.random_int(min=1, max=50)),
            "other_order_item_details": fake.sentence(nb_words=10)
        }
        data.append(order_item)
    return data
