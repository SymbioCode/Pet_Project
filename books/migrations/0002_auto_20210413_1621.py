# Generated by Django 3.2 on 2021-04-13 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_interested',
            field=models.BooleanField(default=False, verbose_name='Є вподобана'),
        ),
        migrations.AddField(
            model_name='book',
            name='user_interested',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Зацікавлений користувач'),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_set_up', to=settings.AUTH_USER_MODEL, verbose_name='Власник'),
        ),
    ]