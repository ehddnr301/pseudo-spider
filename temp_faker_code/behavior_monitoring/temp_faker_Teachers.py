



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "teacher_id": _ + 1,
            "address_id": random.randint(1, 100),
            "first_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(['M', 'F']),
            "cell_mobile_number": fake.phone_number(),
            "email_address": fake.email(),
            "other_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
