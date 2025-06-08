



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "dog_id": _ + 1,
            "owner_id": random.randint(1, 100),
            "abandoned_yn": random.choice(['Y', 'N']),
            "breed_code": fake.word()[:10],
            "size_code": fake.word()[:10],
            "name": fake.first_name(),
            "age": fake.random_int(min=1, max=20),
            "date_of_birth": fake.date_time_this_year(),
            "gender": random.choice(['M', 'F']),
            "weight": f"{fake.random_int(min=1, max=100)} kg",
            "date_arrived": fake.date_time_this_year(),
            "date_adopted": fake.date_time_this_year(),
            "date_departed": fake.date_time_this_year()
        }
        data.append(record)
    return data
