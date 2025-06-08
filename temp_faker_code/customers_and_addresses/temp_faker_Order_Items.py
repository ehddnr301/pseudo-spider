



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        order_id = random.randint(1, 1000)
        product_id = random.randint(1, 1000)
        order_quantity = str(random.randint(1, 100))  # VARCHAR(15)로 변환
        data.append({
            "order_id": order_id,
            "product_id": product_id,
            "order_quantity": order_quantity
        })
    return data
