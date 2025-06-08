



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "payment_id": fake.random_int(min=1, max=10000),
            "booking_id": fake.random_int(min=1, max=10000),
            "customer_id": fake.random_int(min=1, max=10000),
            "payment_type_code": fake.random_element(elements=("CREDIT", "DEBIT", "CASH", "PAYPAL")),
            "amount_paid_in_full_yn": fake.random_element(elements=("Y", "N")),
            "payment_date": fake.date_time_this_year(),
            "amount_due": round(fake.random_number(digits=5) + fake.random.random(), 4),
            "amount_paid": round(fake.random_number(digits=5) + fake.random.random(), 4)
        }
        data.append(record)
    return data
