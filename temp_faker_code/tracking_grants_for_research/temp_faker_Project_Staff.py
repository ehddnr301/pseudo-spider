



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": fake.random_number(digits=5, fix_len=True),
            "project_id": fake.random_int(min=1, max=100),
            "role_code": fake.random_element(elements=("DEV", "QA", "PM", "UX")),
            "date_from": fake.date_time_this_year(),
            "date_to": fake.date_time_this_year(),
            "other_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
