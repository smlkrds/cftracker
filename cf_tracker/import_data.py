import csv
import os

import django
import psycopg2

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cf_tracker.settings')
django.setup()

# Connect to PostgreSQL database hosted on Railway
conn = psycopg2.connect(
    dbname='railway',
    user='postgres',
    password='TdiyyKm8pHwnLkI161T8',
    host='containers-us-west-137.railway.app',
    port='7036',
)

# Open CSV file
with open('food-footprints.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Extract data from CSV row
        field1 = row['Entity']
        field2 = row['Code']
        field3 = row['Year']
        field4 = row['GHG emissions per kilogram (Poore & Nemecek, 2018)']

        # Save data to PostgreSQL using Django ORM
        from api.models import Food

        obj = Food(
            entity=field1,
            code=field2,
            year=field3,
            co2_equivalent_per_kg=field4,
        )
        obj.save()

# Close database connection
conn.close()