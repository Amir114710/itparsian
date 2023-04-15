# Generated by Django 4.1.7 on 2023-04-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_alter_services_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="tipsabout",
            name="first_col",
            field=models.BooleanField(
                default=False, verbose_name="ایا در ستون اول باشد ؟"
            ),
        ),
        migrations.AddField(
            model_name="tipsabout",
            name="seconde_col",
            field=models.BooleanField(
                default=False, verbose_name="ایا در ستون دوم باشد ؟"
            ),
        ),
    ]
