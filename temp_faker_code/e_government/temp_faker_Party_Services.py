



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "booking_id": random.randint(1, 1000),
            "customer_id": random.randint(1, 1000),
            "service_id": random.randint(1, 1000),
            "service_datetime": fake.date_time_this_year(),
            "booking_made_date": fake.date_time_this_year() 
        }
        data.append(record)
    return data
