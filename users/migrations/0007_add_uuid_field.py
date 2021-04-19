# Generated by Django 3.0.5 on 2021-01-15 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210115_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]