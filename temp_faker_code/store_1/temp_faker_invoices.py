



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "customer_id": random.randint(1, 1000),
            "invoice_date": fake.date_time_this_year(),
            "billing_address": fake.street_address(),
            "billing_city": fake.city(),
            "billing_state": fake.state(),
            "billing_country": fake.country(),
            "billing_postal_code": fake.zipcode(),
            "total": round(random.uniform(10.00, 1000.00), 2)
        }
        data.append(record)
    
    return data
