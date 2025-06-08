



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Claim_ID": fake.random_int(min=1, max=10000),
            "Document_Type_Code": fake.lexify(text='???'),
            "Created_by_Staff_ID": fake.random_int(min=1, max=1000),
            "Created_Date": int(fake.date_time_this_year().timestamp())
        }
        data.append(record)
    return data
