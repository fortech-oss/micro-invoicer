# Generated by Django 4.1.1 on 2023-01-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("microinvoicer", "0030_alter_microregistry_include_vat"),
    ]

    operations = [
        migrations.AddField(
            model_name="timeinvoice",
            name="include_vat",
            field=models.IntegerField(default=0),
        ),
    ]