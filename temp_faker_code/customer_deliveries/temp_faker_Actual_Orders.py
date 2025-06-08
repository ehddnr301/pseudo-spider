



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "actual_order_id": _ + 1,
            "order_status_code": fake.random_element(elements=("Pending", "Shipped", "Delivered", "Cancelled")),
            "regular_order_id": random.randint(1, 1000),
            "actual_order_date": fake.date_time_this_year()
        }
        data.append(record)
    
    return data
