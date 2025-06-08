



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "rental_id": _ + 1,
            "rental_date": fake.date_time_this_year(),
            "inventory_id": random.randint(1, 16777215),  # MEDIUMINT UNSIGNED
            "customer_id": random.randint(1, 65535),      # SMALLINT UNSIGNED
            "return_date": fake.date_time_this_year() ,
            "staff_id": random.randint(1, 255),           # TINYINT UNSIGNED
            "last_update": fake.date_time_this_year(),
        }
        data.append(record)
    
    return data
