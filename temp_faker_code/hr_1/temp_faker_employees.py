



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "EMPLOYEE_ID": random.randint(1, 999999),
            "FIRST_NAME": fake.first_name(),
            "LAST_NAME": fake.last_name(),
            "EMAIL": fake.email(),
            "PHONE_NUMBER": fake.phone_number(),
            "HIRE_DATE": fake.date_time_this_year().date(),
            "JOB_ID": fake.word()[:10],
            "SALARY": round(random.uniform(30000, 120000), 2),
            "COMMISSION_PCT": round(random.uniform(0, 0.5), 2) ,
            "MANAGER_ID": random.randint(1, 999999) ,
            "DEPARTMENT_ID": random.randint(1, 9999) 
        }
        data.append(record)
    return data
