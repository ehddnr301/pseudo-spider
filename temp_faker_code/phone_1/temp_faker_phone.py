



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Company_name": fake.company(),
            "Hardware_Model_name": fake.word(),
            "Accreditation_type": fake.word(),
            "Accreditation_level": fake.word(),
            "Date": fake.date_time_this_year().isoformat(),
            "chip_model": fake.word(),
            "screen_mode": random.choice(['LCD', 'OLED', 'AMOLED'])
        }
        data.append(record)
    return data
