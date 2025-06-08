



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": random.randint(1, 1000),
            "department_id": random.randint(1, 100),
            "date_assigned_from": fake.date_time_this_year(),
            "job_title_code": fake.lexify(text='??????'),
            "date_assigned_to": fake.date_time_this_year() 
        }
        data.append(record)
    return data
