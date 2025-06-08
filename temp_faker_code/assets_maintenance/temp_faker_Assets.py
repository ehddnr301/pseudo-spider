


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "asset_id": _ + 1,
            "maintenance_contract_id": random.randint(1, 100),
            "supplier_company_id": random.randint(1, 100),
            "asset_details": fake.sentence(),
            "asset_make": fake.word(),
            "asset_model": fake.word(),
            "asset_acquired_date": fake.date_time_this_year(),
            "asset_disposed_date": fake.date_time_this_year() ,
            "other_asset_details": fake.sentence()
        }
        data.append(record)
    return data
