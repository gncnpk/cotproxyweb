# Generated by Django 4.1.7 on 2023-03-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cpweb", "0004_video_cptransform_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="queue",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="queue",
            name="queue",
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="route",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
