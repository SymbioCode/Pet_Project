# Generated by Django 3.2 on 2021-04-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_is_allowed_to_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_exchanged',
            field=models.BooleanField(default=False, verbose_name='Була обміняна'),
        ),
    ]
