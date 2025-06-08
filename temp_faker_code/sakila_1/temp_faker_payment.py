



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "payment_id": random.randint(1, 65535),
            "customer_id": random.randint(1, 65535),
            "staff_id": random.randint(0, 255),
            "rental_id": random.choice([random.randint(1, 2147483647), None]),
            "amount": round(random.uniform(0, 999.99), 2),
            "payment_date": fake.date_time_this_year(),
            "last_update": datetime.now()
        }
        record["rental_id"] = record["rental_id"] if record["rental_id"] is not None else random.randint(1, 2147483647)
        data.append(record)
    return data
