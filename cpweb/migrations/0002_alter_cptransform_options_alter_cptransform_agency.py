# Generated by Django 4.0.3 on 2022-05-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cpweb", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cptransform",
            options={
                "ordering": ["callsign", "cot_uid"],
                "verbose_name": "Transform",
                "verbose_name_plural": "Transforms",
            },
        ),
        migrations.AlterField(
            model_name="cptransform",
            name="agency",
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
