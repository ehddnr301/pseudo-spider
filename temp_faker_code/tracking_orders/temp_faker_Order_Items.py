



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        order_item = {
            "order_item_id": _ + 1,
            "product_id": random.randint(1, 100),
            "order_id": random.randint(1, 100),
            "order_item_status": fake.random_element(elements=("Pending", "Shipped", "Delivered", "Cancelled")),
            "order_item_details": fake.text(max_nb_chars=255)
        }
        data.append(order_item)
    return data
