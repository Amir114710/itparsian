# Generated by Django 4.1.7 on 2023-04-17 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_rename_parent_id_comment_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="email",
        ),
    ]