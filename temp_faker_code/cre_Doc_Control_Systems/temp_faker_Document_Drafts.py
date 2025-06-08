


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        document_id = random.randint(1, 1000)
        draft_number = random.randint(1, 10)
        draft_details = fake.text(max_nb_chars=255)
        
        data.append({
            "document_id": document_id,
            "draft_number": draft_number,
            "draft_details": draft_details
        })
    return data
