



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        order_item = {
            "order_item_id": fake.unique.random_int(min=1, max=1000),
            "order_id": fake.unique.random_int(min=1, max=1000),
            "product_id": fake.unique.random_int(min=1, max=1000),
            "order_quantity": str(fake.random_int(min=1, max=100))
        }
        data.append(order_item)
    return data
