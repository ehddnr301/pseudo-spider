



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CLASS_CODE": fake.bothify(text='??###'),
            "CRS_CODE": fake.bothify(text='???-#####'),
            "CLASS_SECTION": fake.random_element(elements=('A', 'B', 'C', 'D')),
            "CLASS_TIME": fake.date_time_this_year().strftime("%H:%M"),
            "CLASS_ROOM": fake.bothify(text='###-###'),
            "PROF_NUM": random.randint(1, 100)
        }
        data.append(record)
    return data
