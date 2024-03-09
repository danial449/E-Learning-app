# Generated by Django 4.1 on 2024-03-05 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("teachers", "0008_alter_feedback_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="created_date",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
    ]
