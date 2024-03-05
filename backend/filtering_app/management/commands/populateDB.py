import csv
from django.core.management.base import BaseCommand
from filtering_app.models import YelpData  # Import your model

class Command(BaseCommand):
    help = 'Import data from a CSV file to the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        # Open and read the CSV file
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            
    # business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,categories

            # Iterate through each row in the CSV and save it to the database
            for row in reader:
                YelpData.objects.create(
                    business_id=row['business_id'],
                    name=row['name'],
                    address=row['address'],
                    city=row['city'],
                    state=row['state'],
                    postal_code=row['postal_code'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    stars=row['stars'],
                    review_count=row['review_count'],
                    is_open=row['is_open'],
                    categories=row['categories'],
                    
                    # Map CSV columns to your model fields
                )
                

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
