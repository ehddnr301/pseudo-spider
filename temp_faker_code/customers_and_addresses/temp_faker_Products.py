



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        product_id = random.randint(1, 1000)
        product_details = fake.text(max_nb_chars=255)
        data.append({
            "product_id": product_id,
            "product_details": product_details
        })
    return data
