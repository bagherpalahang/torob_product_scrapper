# Generated by Django 4.2.1 on 2023-07-16 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edqam_page_scrapper', '0009_edghampage_created_edghampage_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edghampage',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='edghampage',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]