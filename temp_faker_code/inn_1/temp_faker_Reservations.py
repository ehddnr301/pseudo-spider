



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Code": _ + 1,
            "Room": fake.word(),
            "CheckIn": fake.date_time_this_year().isoformat(),
            "CheckOut": fake.date_time_this_year().isoformat(),
            "Rate": round(random.uniform(50.0, 500.0), 2),
            "LastName": fake.last_name(),
            "FirstName": fake.first_name(),
            "Adults": random.randint(1, 4),
            "Kids": random.randint(0, 3)
        }
        data.append(record)
    
    return data
