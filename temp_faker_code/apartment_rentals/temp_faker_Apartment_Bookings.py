



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "apt_booking_id": _ + 1,
            "apt_id": random.randint(1, 100),
            "guest_id": random.randint(1, 1000),
            "booking_status_code": fake.random_element(elements=("confirmed", "pending", "cancelled")),
            "booking_start_date": fake.date_time_this_year(),
            "booking_end_date": fake.date_time_this_year(),
        }
        data.append(record)
    
    return data
