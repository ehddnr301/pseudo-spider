



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "duration": random.randint(1, 1000),
            "start_date": fake.date_time_this_year().isoformat(),
            "start_station_name": fake.city(),
            "start_station_id": random.randint(1, 100),
            "end_date": fake.date_time_this_year().isoformat(),
            "end_station_name": fake.city(),
            "end_station_id": random.randint(1, 100),
            "bike_id": random.randint(1, 500),
            "subscription_type": random.choice(['Subscriber', 'Customer']),
            "zip_code": fake.zipcode()
        }
        data.append(record)
    return data
