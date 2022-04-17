# Generated by Django 2.2.13 on 2022-04-14 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_favoriteitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
