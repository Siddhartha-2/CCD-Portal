# Generated by Django 3.0.3 on 2020-02-21 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200220_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='company_name',
        ),
    ]