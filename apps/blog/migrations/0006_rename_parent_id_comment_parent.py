# Generated by Django 4.1.7 on 2023-04-17 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_rename_parent_comment_parent_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="parent_id",
            new_name="parent",
        ),
    ]
