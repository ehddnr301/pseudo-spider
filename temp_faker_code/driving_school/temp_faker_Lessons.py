



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "lesson_id": _ + 1,
            "customer_id": random.randint(1, 100),
            "lesson_status_code": fake.random_element(elements=("scheduled", "completed", "canceled")),
            "staff_id": random.choice([None, random.randint(1, 50)]),
            "vehicle_id": random.randint(1, 100),
            "lesson_date": fake.date_time_this_year(),
            "lesson_time": fake.time(),
            "price": round(random.uniform(20.0, 200.0), 2)
        }
        data.append(record)
    
    return data
