



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "student_id": random.randint(1, 1000),
            "address_id": random.randint(1, 100),
            "first_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "last_name": fake.last_name(),
            "cell_mobile_number": fake.phone_number(),
            "email_address": fake.email(),
            "date_first_rental": fake.date_time_this_year(),
            "date_left_university": fake.date_time_this_year(),
            "other_student_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
