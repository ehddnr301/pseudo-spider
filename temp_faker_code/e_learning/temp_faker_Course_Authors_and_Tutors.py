



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "author_id": _ + 1,
            "author_tutor_ATB": fake.random_element(elements=('AT', 'TB', '')),
            "login_name": fake.user_name(),
            "password": fake.password(),
            "personal_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "family_name": fake.last_name(),
            "gender_mf": fake.random_element(elements=('M', 'F')),
            "address_line_1": fake.address().replace("\n", ", ")
        }
        data.append(record)
    return data
