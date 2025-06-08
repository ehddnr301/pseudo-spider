



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "customer_id": fake.random_int(min=1, max=1000),
            "datetime_payment": fake.date_time_this_year(),
            "payment_method_code": fake.random_element(elements=("CASH", "CREDIT", "DEBIT")),
            "amount_payment": round(random.uniform(1.0, 1000.0), 2)
        }
        data.append(record)
    
    return data
