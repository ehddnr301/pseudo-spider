



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "last_name": fake.last_name(),
            "first_name": fake.first_name(),
            "title": fake.job(),
            "reports_to": random.choice([None, _]) if _ > 0 else None,
            "birth_date": fake.date_time_this_year(),
            "hire_date": fake.date_time_this_year(),
            "address": fake.address(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country(),
            "postal_code": fake.zipcode(),
            "phone": fake.phone_number(),
            "fax": fake.phone_number(),
            "email": fake.email()
        }
        data.append(record)
    
    return data
