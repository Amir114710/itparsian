# Generated by Django 4.1.7 on 2023-04-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_remove_comment_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="ایمیل"
            ),
        ),
    ]
