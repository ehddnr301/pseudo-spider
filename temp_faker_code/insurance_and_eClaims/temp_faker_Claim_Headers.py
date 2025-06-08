


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Claim_Header_ID": fake.random_int(min=1, max=10000),
            "Claim_Status_Code": fake.lexify(text='?????'),
            "Claim_Type_Code": fake.lexify(text='?????'),
            "Policy_ID": fake.random_int(min=1, max=10000),
            "Date_of_Claim": fake.date_time_this_year(),
            "Date_of_Settlement": fake.date_time_this_year(),
            "Amount_Claimed": round(fake.random_number(digits=20), 4),
            "Amount_Piad": round(fake.random_number(digits=20), 4)
        }
        data.append(record)
    return data
