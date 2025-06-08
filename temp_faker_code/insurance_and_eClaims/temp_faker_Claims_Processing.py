



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Claim_Processing_ID": fake.unique.random_int(min=1, max=10000),
            "Claim_ID": fake.unique.random_int(min=1, max=10000),
            "Claim_Outcome_Code": fake.lexify(text='?????'),
            "Claim_Stage_ID": fake.random_int(min=1, max=10),
            "Staff_ID": fake.random_int(min=1, max=100) 
        }
        data.append(record)
    return data
