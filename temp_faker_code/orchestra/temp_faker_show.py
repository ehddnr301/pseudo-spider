



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Show_ID": fake.random_int(min=1, max=1000),
            "Performance_ID": fake.random_int(min=1, max=1000),
            "If_first_show": fake.boolean(),
            "Result": fake.text(max_nb_chars=200),
            "Attendance": round(fake.random_number(digits=3) / 100, 2)
        }
        data.append(record)
    return data
