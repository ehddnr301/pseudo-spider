



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "EMP_NUM": random.randint(1, 1000),
            "EMP_LNAME": fake.last_name(),
            "EMP_FNAME": fake.first_name(),
            "EMP_INITIAL": fake.random_letter().upper(),
            "EMP_JOBCODE": fake.bothify(text='??###'),
            "EMP_HIREDATE": fake.date_time_this_year(),
            "EMP_DOB": fake.date_time_this_year()
        }
        data.append(record)
    return data
