



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "shipment_id": random.randint(1, 1000),
            "order_id": random.randint(1, 1000),
            "invoice_number": random.randint(1, 1000),
            "shipment_tracking_number": fake.bothify(text='??-#####'),
            "shipment_date": fake.date_time_this_year(),
            "other_shipment_details": fake.sentence()
        }
        data.append(record)
    
    return data
