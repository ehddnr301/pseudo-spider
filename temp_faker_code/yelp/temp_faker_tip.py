



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year_month = fake.date_time_this_year()
        data.append({
            "tip_id": _ + 1,
            "business_id": fake.uuid4(),
            "text": fake.text(),
            "user_id": fake.uuid4(),
            "likes": random.randint(0, 100),
            "year": year_month.year,
            "month": year_month.strftime("%B")
        })
    return data
