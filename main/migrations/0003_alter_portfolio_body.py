# Generated by Django 5.0.6 on 2024-05-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_services_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
