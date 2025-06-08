



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": _ + 1,
            "product": fake.word(),
            "dimensions": f"{random.randint(1, 100)}x{random.randint(1, 100)}x{random.randint(1, 100)}",
            "dpi": round(random.uniform(100, 1200), 2),
            "pages_per_minute_color": round(random.uniform(1, 50), 2),
            "max_page_size": f"{random.randint(1, 100)}x{random.randint(1, 100)}",
            "interface": fake.word()
        }
        data.append(record)
    return data
