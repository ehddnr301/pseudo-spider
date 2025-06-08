



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        entry = {
            "fault_log_entry_id": _ + 1,
            "asset_id": random.randint(1, 100),
            "recorded_by_staff_id": random.randint(1, 50),
            "fault_log_entry_datetime": fake.date_time_this_year(),
            "fault_description": fake.sentence(),
            "other_fault_details": fake.sentence()
        }
        data.append(entry)
    
    return data
