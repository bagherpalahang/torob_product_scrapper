# Generated by Django 4.2.1 on 2023-07-16 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edqam_page_scrapper', '0007_alter_edghampage_page_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edghampage',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_edghamPage', to=settings.AUTH_USER_MODEL),
        ),
    ]
