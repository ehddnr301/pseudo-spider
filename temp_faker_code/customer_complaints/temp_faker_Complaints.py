



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "complaint_id": random.randint(1, 1000),
            "product_id": random.randint(1, 100),
            "customer_id": random.randint(1, 500),
            "complaint_outcome_code": fake.word(),
            "complaint_status_code": fake.word(),
            "complaint_type_code": fake.word(),
            "date_complaint_raised": fake.date_time_this_year(),
            "date_complaint_closed": fake.date_time_this_year(),
            "staff_id": random.randint(1, 50)
        }
        data.append(record)
    return data
