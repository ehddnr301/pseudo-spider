



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        area_code = random.randint(100, 999)
        state = fake.state_abbr()
        
        data.append({
            "area_code": area_code,
            "state": state
        })
    
    return data
