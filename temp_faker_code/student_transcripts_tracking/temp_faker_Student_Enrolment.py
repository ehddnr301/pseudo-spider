



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "student_enrolment_id": _ + 1,
            "degree_program_id": random.randint(1, 10),
            "semester_id": random.randint(1, 8),
            "student_id": random.randint(1, 1000),
            "other_details": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
