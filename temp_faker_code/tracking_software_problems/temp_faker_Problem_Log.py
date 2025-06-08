



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "problem_log_id": _ + 1,
            "assigned_to_staff_id": random.randint(1, 100),
            "problem_id": random.randint(1, 100),
            "problem_category_code": fake.word(),
            "problem_status_code": fake.word(),
            "log_entry_date": fake.date_time_this_year(),
            "log_entry_description": fake.sentence(),
            "log_entry_fix": fake.sentence(),
            "other_log_details": fake.sentence()
        }
        data.append(record)
    return data
