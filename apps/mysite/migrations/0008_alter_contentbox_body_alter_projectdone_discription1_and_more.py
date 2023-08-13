# Generated by Django 4.2.3 on 2023-08-12 14:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0007_alter_services_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contentbox",
            name="body",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="projectdone",
            name="discription1",
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=70),
        ),
        migrations.AlterField(
            model_name="projectdone",
            name="discription2",
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=70),
        ),
        migrations.AlterField(
            model_name="projectdone",
            name="title",
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name="services",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]