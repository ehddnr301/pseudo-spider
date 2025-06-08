



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        employee_id = fake.random_int(min=100000, max=999999)
        start_date = fake.date_time_this_year().date()
        end_date = fake.date_time_this_year().date()
        job_id = fake.lexify(text='??????')
        department_id = fake.random_int(min=1000, max=9999)
        
        data.append({
            "EMPLOYEE_ID": employee_id,
            "START_DATE": start_date,
            "END_DATE": end_date,
            "JOB_ID": job_id,
            "DEPARTMENT_ID": department_id
        })
    return data
