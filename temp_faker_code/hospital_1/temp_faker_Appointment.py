



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        appointment = {
            "AppointmentID": _ + 1,
            "Patient": random.randint(1, 100),
            "PrepNurse": random.randint(1, 10) ,
            "Physician": random.randint(1, 50),
            "Start": fake.date_time_this_year(),
            "End": fake.date_time_this_year(),
            "ExaminationRoom": fake.word()
        }
        data.append(appointment)
    return data
