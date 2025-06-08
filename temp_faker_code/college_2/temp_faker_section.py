



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "course_id": fake.bothify(text='??######'),
            "sec_id": fake.bothify(text='??######'),
            "semester": fake.random_element(elements=('Fall', 'Spring', 'Summer')),
            "year": fake.year(),
            "building": fake.word()[:15],
            "room_number": fake.bothify(text='###'),
            "time_slot_id": fake.bothify(text='####')
        }
        data.append(record)
    return data
