



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "maintenance_contract_id": _ + 1,
            "maintenance_contract_company_id": random.randint(1, 100),
            "contract_start_date": fake.date_time_this_year(),
            "contract_end_date": fake.date_time_this_year(),
            "other_contract_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    
    return data
