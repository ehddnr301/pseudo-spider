


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        organization_id = fake.unique.random_int(min=1, max=1000)
        parent_organization_id = fake.random_int(min=1, max=1000) 
        organization_details = fake.text(max_nb_chars=255) 
        
        data.append({
            "organization_id": organization_id,
            "parent_organization_id": parent_organization_id,
            "organization_details": organization_details
        })
    return data
