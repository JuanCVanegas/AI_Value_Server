# Generated by Django 3.0.6 on 2020-05-28 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_person_fullname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
