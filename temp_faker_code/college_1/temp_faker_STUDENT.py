



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "STU_NUM": _ + 1,
            "STU_LNAME": fake.last_name(),
            "STU_FNAME": fake.first_name(),
            "STU_INIT": fake.random_letter().upper(),
            "STU_DOB": fake.date_time_this_year(),
            "STU_HRS": random.randint(1, 20),
            "STU_CLASS": fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "STU_GPA": round(random.uniform(0.0, 4.0), 2),
            "STU_TRANSFER": random.uniform(0, 1),
            "DEPT_CODE": fake.bothify(text='??-###'),
            "STU_PHONE": fake.random_int(min=1000, max=9999),
            "PROF_NUM": random.randint(1, 10)
        }
        data.append(record)
    return data
