# Generated by Django 4.1.7 on 2023-02-22 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_rename_rate_our_products_and_service_form_rate_our_internship_and_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Rate_our_Internship_and_services',
            new_name='Rate_our_Products_and_services',
        ),
    ]
