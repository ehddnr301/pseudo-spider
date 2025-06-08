



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Policy_ID": random.randint(1, 1000),
            "policy_type_code": fake.lexify(text='?????'),
            "Customer_Phone": fake.phone_number()
        }
        data.append(record)
    return data
