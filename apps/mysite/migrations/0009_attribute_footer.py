# Generated by Django 4.2.3 on 2023-08-12 21:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "mysite",
            "0008_alter_contentbox_body_alter_projectdone_discription1_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Attribute",
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
                ("title", models.CharField(max_length=250, verbose_name="نام ویژگی")),
                ("created", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "ویژگی ها",
                "verbose_name_plural": "ویژگی های سایت",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Footer",
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
                (
                    "address",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="ادرس"
                    ),
                ),
                (
                    "phone_number",
                    models.IntegerField(default=0, verbose_name="شماره تلفن"),
                ),
                (
                    "whatsappphone_number",
                    models.CharField(max_length=50, verbose_name="شماره تلفن واتساپ"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="ایمیل")),
                (
                    "discription",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="توضیحات"
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "attribute",
                    models.ManyToManyField(
                        related_name="footers",
                        to="mysite.attribute",
                        verbose_name="ویژگی",
                    ),
                ),
            ],
            options={
                "verbose_name": "فوتر",
                "verbose_name_plural": "فوتر",
                "ordering": ["-created"],
            },
        ),
    ]
