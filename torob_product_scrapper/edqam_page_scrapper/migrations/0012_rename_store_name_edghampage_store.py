# Generated by Django 4.2.3 on 2023-07-20 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edqam_page_scrapper', '0011_edghampage_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edghampage',
            old_name='store_name',
            new_name='store',
        ),
    ]
