# Generated by Django 3.1.7 on 2021-03-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210310_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='pass_id',
        ),
        migrations.AlterField(
            model_name='user_data',
            name='pass_email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]