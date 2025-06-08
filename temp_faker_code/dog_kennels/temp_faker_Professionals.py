



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "professional_id": _ + 1,
            "role_code": fake.random_element(elements=("Doctor", "Nurse", "Technician", "Administrator")),
            "first_name": fake.first_name(),
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip_code": fake.zipcode(),
            "last_name": fake.last_name(),
            "email_address": fake.email(),
            "home_phone": fake.phone_number(),
            "cell_number": fake.phone_number()
        }
        data.append(record)
    return data
