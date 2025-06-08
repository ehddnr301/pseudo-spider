



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 1000),
            "channel_code": fake.lexify(text='?????'),
            "active_from_date": fake.date_time_this_year(),
            "active_to_date": fake.date_time_this_year(),
            "contact_number": fake.phone_number()
        }
        data.append(record)
    
    return data
