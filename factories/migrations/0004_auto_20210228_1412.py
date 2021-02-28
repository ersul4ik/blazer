# Generated by Django 3.1.5 on 2021-02-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factories', '0003_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafixturecolumn',
            name='sample',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Full name'), (2, 'Integer'), (3, 'Company'), (4, 'Address'), (5, 'Job'), (6, 'Email'), (7, 'Phone number'), (8, 'Domain name'), (10, 'Date')]),
        ),
    ]