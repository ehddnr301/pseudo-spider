



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "guest_id": _ + 1,
            "gender_code": random.choice(['M', 'F']),
            "guest_first_name": fake.first_name(),
            "guest_last_name": fake.last_name(),
            "date_of_birth": fake.date_time_this_year()
        }
        data.append(record)
    
    return data
