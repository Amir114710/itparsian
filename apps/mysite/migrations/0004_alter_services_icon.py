# Generated by Django 4.1.7 on 2023-04-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0003_tipsabout"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="icon",
            field=models.FileField(upload_to="ServicesLogo"),
        ),
    ]
