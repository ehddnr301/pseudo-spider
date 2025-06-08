



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "party_id": random.randint(1, 1000),
            "form_id": random.randint(1, 1000),
            "date_completion_started": fake.date_time_this_year(),
            "form_status_code": fake.word()[:15],
            "date_fully_completed": fake.date_time_this_year() 
        }
        data.append(record)
    return data
