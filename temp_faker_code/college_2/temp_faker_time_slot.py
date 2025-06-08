



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        time_slot_id = fake.bothify(text='??##')
        day = random.choice(['M', 'T', 'W', 'R', 'F', 'S', 'U'])
        start_time = fake.date_time_this_year()
        start_hr = start_time.hour % 24
        start_min = start_time.minute % 60
        end_hr = (start_hr + random.randint(1, 3)) % 24
        end_min = random.choice([0, 15, 30, 45])
        
        data.append({
            'time_slot_id': time_slot_id,
            'day': day,
            'start_hr': start_hr,
            'start_min': start_min,
            'end_hr': end_hr,
            'end_min': end_min
        })
    
    return data
