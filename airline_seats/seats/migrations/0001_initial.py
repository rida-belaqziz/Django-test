# Generated by Django 4.2.16 on 2024-10-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Seat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seat_number", models.CharField(max_length=10, unique=True)),
                ("is_occupied", models.BooleanField(default=False)),
            ],
        ),
    ]
