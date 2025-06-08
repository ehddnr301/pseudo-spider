#!/bin/bash

echo "첫번째"

python create_database.py

echo "두번째"

python create_ddl.py

echo "세번째"

python execute_ddl.py

echo "네번째"

python generate_fake_data.py

echo "다섯번째"

python remove_unnecessary.py

echo "여섯번째"

python data_inserter.py

echo "일곱번째"

python find_empty_tables.py

echo "여덟번째"

python generate_fake_yaml.py