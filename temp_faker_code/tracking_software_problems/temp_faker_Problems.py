



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "problem_id": _ + 1,
            "product_id": random.randint(1, 100),
            "closure_authorised_by_staff_id": random.randint(1, 100),
            "reported_by_staff_id": random.randint(1, 100),
            "date_problem_reported": fake.date_time_this_year(),
            "date_problem_closed": fake.date_time_this_year() ,
            "problem_description": fake.sentence() ,
            "other_problem_details": fake.sentence() 
        }
        data.append(record)
    return data
