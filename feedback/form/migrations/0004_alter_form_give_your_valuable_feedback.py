# Generated by Django 4.1.7 on 2023-02-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_alter_form_email_alter_form_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Give_Your_Valuable_Feedback',
            field=models.CharField(default='', max_length=200),
        ),
    ]
