# Generated by Django 3.1.5 on 2021-02-28 06:56

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('column_separator', models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)')], default=',', max_length=5)),
                ('string_character', models.CharField(choices=[("''", "Single quote ('')"), ('""', 'Double quote ("")')], default='""', max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Data fixture',
                'verbose_name_plural': 'Data fixtures',
            },
        ),
        migrations.CreateModel(
            name='DataFixtureColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('sample', models.PositiveSmallIntegerField(choices=[(1, 'Full name'), (2, 'Integer'), (3, 'Company'), (4, 'Address')])),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('extra', django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='factories.datafixture')),
            ],
        ),
    ]
