



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "student_id": random.randint(1, 1000),
            "address_id": random.randint(1, 1000),
            "date_address_from": fake.date_time_this_year(),
            "date_address_to": fake.date_time_this_year(),
            "monthly_rental": round(random.uniform(500, 2000), 4),
            "other_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    
    return data
