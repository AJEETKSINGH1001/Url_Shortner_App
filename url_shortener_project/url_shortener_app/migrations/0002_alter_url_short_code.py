# Generated by Django 4.2.7 on 2023-12-10 05:59

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_code',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22, unique=True),
        ),
    ]
