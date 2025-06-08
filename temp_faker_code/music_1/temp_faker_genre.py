



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "g_name": fake.word()[:20],  # varchar2(20)
            "rating": random.choice(['G', 'PG', 'PG-13', 'R', 'NC-17']),  # varchar2(10)
            "most_popular_in": fake.city()[:50]  # varchar2(50)
        }
        data.append(record)
    
    return data
