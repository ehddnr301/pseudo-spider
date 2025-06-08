



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "party_id": _ + 1,
            "payment_method_code": fake.random_element(elements=("CREDIT_CARD", "DEBIT_CARD", "PAYPAL")),
            "party_phone": fake.phone_number(),
            "party_email": fake.email()
        }
        data.append(record)
    return data
