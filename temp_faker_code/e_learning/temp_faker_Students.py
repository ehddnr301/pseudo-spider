



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "student_id": random.randint(1, 1000),
            "date_of_registration": fake.date_time_this_year(),
            "date_of_latest_logon": fake.date_time_this_year(),
            "login_name": fake.user_name(),
            "password": fake.password(length=10),
            "personal_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "family_name": fake.last_name()
        }
        data.append(record)
    return data
