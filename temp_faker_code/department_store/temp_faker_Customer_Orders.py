



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "order_id": random.randint(1, 1000),
            "customer_id": random.randint(1, 100),
            "order_status_code": fake.random_element(elements=("Pending", "Shipped", "Delivered", "Cancelled")),
            "order_date": fake.date_time_this_year()
        }
        data.append(record)
    return data
