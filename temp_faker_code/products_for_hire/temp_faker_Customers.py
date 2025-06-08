



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": _ + 1,
            "coupon_id": random.randint(1, 100),
            "good_or_bad_customer": random.choice(['good', 'bad']),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender_mf": random.choice(['M', 'F']),
            "date_became_customer": fake.date_time_this_year(),
            "date_last_hire": fake.date_time_this_year()
        }
        data.append(record)
    return data
