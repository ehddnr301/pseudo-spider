



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year_month = fake.date_time_this_year()
        data.append({
            "rid": _ + 1,
            "business_id": fake.uuid4(),
            "user_id": fake.uuid4(),
            "rating": round(random.uniform(1, 5), 1),
            "text": fake.text(max_nb_chars=200),
            "year": year_month.year,
            "month": year_month.strftime("%B")
        })
    return data
