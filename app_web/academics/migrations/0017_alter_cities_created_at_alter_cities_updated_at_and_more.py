# Generated by Django 5.0.2 on 2024-04-05 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0016_person_id_user_alter_cities_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='cpuntries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='cpuntries',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='identification_types',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 415032)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 398445)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 412067)),
        ),
        migrations.AlterField(
            model_name='students',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 412067)),
        ),
        migrations.AlterField(
            model_name='students',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 412067)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 398445)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 27, 4, 412067)),
        ),
    ]