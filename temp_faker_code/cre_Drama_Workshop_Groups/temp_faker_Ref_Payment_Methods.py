



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        payment_method_code = fake.bothify(text='??######')  # CHAR(10)
        payment_method_description = fake.sentence(nb_words=6)  # VARCHAR(80)
        
        data.append({
            "payment_method_code": payment_method_code,
            "payment_method_description": payment_method_description
        })
    
    return data
