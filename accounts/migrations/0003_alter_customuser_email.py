# Generated by Django 4.1 on 2024-03-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0002_customuser_email_verification_token_customuser_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]