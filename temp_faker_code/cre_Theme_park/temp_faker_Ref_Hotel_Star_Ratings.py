



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        star_rating_code = fake.bothify(text='??###')  # CHAR(15) 형식에 맞게 생성
        star_rating_description = fake.sentence(nb_words=6)  # VARCHAR(80) 형식에 맞게 생성
        
        data.append({
            "star_rating_code": star_rating_code,
            "star_rating_description": star_rating_description
        })
    
    return data
