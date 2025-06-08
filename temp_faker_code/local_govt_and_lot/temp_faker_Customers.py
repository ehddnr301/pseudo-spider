



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        customer_id = random.randint(1, 1000)
        customer_details = fake.sentence(nb_words=10)
        data.append({
            "customer_id": customer_id,
            "customer_details": customer_details
        })
    return data
