# Generated by Django 4.1.7 on 2023-04-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0005_tipsabout_first_col_tipsabout_seconde_col"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contentbox",
            options={
                "ordering": ["-created"],
                "verbose_name": "کانتنت باکس های سایت",
                "verbose_name_plural": "کانتنت باکس های سایت",
            },
        ),
        migrations.AlterModelOptions(
            name="mainmenu",
            options={
                "ordering": ["-created"],
                "verbose_name": "منو های سایت",
                "verbose_name_plural": "منو های سایت",
            },
        ),
        migrations.AlterModelOptions(
            name="projectdone",
            options={
                "ordering": ["-created"],
                "verbose_name": "نمونه کار های سایت",
                "verbose_name_plural": "نمونه کار های سایت",
            },
        ),
        migrations.AlterModelOptions(
            name="services",
            options={
                "ordering": ["-created"],
                "verbose_name": "سرویس های سایت",
                "verbose_name_plural": "سرویس های سایت",
            },
        ),
        migrations.AddField(
            model_name="contentbox",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="mainmenu",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="projectdone",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="services",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="tipsabout",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
