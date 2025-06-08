



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "location_code": fake.lexify(text='?????'),
            "actual_order_id": random.randint(1, 1000),
            "delivery_status_code": fake.lexify(text='?????'),
            "driver_employee_id": random.randint(1, 100),
            "truck_id": random.randint(1, 100),
            "delivery_date": fake.date_time_this_year()
        }
        data.append(record)
    
    return data
