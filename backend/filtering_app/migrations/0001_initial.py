# Generated by Django 4.2.3 on 2024-03-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YelpData',
            fields=[
                ('business_id', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('postal_code', models.CharField(max_length=150)),
                ('latitude', models.CharField(max_length=150)),
                ('longitude', models.CharField(max_length=150)),
                ('stars', models.CharField(max_length=150)),
                ('review_count', models.IntegerField()),
                ('is_open', models.BooleanField(default=False)),
                ('categories', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'YelpData',
            },
        ),
    ]