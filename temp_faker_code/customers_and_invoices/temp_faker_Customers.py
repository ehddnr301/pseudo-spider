



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": _ + 1,
            "customer_first_name": fake.first_name(),
            "customer_middle_initial": fake.random_letter().upper(),
            "customer_last_name": fake.last_name(),
            "gender": random.choice(['M', 'F']),
            "email_address": fake.email(),
            "login_name": fake.user_name(),
            "login_password": fake.password(length=10),
            "phone_number": fake.phone_number(),
            "town_city": fake.city(),
            "state_county_province": fake.state(),
            "country": fake.country()
        }
        data.append(record)
    return data
