# Generated by Django 3.1.7 on 2021-03-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_book_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_email', models.EmailField(max_length=254)),
                ('travel_pnr', models.CharField(max_length=12, unique=True)),
                ('travel_date', models.DateField()),
                ('travel_source', models.CharField(max_length=50)),
                ('travel_destination', models.CharField(max_length=50)),
                ('seat_pre', models.CharField(max_length=10)),
                ('seat_meal', models.CharField(max_length=10)),
            ],
        ),
    ]
