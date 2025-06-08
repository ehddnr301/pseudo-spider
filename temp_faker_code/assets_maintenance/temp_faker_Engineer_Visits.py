


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "engineer_visit_id": _ + 1,
            "contact_staff_id": random.randint(1, 100),
            "engineer_id": random.randint(1, 100),
            "fault_log_entry_id": random.randint(1, 100),
            "fault_status": fake.random_element(elements=("open", "closed", "in_progress")),
            "visit_start_datetime": fake.date_time_this_year(),
            "visit_end_datetime": fake.date_time_this_year(),
            "other_visit_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
