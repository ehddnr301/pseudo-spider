



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "customer_id": _ + 1,
            "customer_address_id": random.randint(1, 1000),
            "customer_status_code": fake.random_element(elements=("Active", "Inactive", "Pending")),
            "date_became_customer": fake.date_time_this_year(),
            "date_of_birth": fake.date_time_this_year(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "amount_outstanding": round(random.uniform(0, 10000), 2),
            "email_address": fake.email(),
            "phone_number": fake.phone_number(),
            "cell_mobile_phone_number": fake.phone_number()
        }
        data.append(record)
    
    return data
