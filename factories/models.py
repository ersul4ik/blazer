from random import randrange

from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from faker import Faker


class DataFixture(models.Model):
    COMMA = ','
    SEMICOLON = ';'
    SEPARATORS = (
        (COMMA, 'Comma (,)'),
        (SEMICOLON, 'Semicolon (;)'),
    )
    SINGLE_QUOTE = "''"
    DOUBLE_QUOTE = '""'
    CHARACTERS = (
        (SINGLE_QUOTE, "Single quote ('')"),
        (DOUBLE_QUOTE, 'Double quote ("")'),
    )
    name = models.CharField(max_length=125)
    column_separator = models.CharField(choices=SEPARATORS, default=COMMA, max_length=5)
    string_character = models.CharField(choices=CHARACTERS, default=DOUBLE_QUOTE, max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Data fixture'
        verbose_name_plural = 'Data fixtures'

    def prepare_fake_data(self):
        return [column.generate_fake_data() for column in self.columns.all()]


class DataFixtureColumn(models.Model):
    FULL_NAME = 1
    INTEGER = 2
    COMPANY_NAME = 3
    ADDRESS = 4
    JOB = 5
    EMAIL = 6
    PHONE_NUMBER = 7
    DOMAIN = 8
    TEXT = 9
    DATE = 10
    SAMPLES = (
        (FULL_NAME, 'Full name'),
        (INTEGER, 'Integer'),
        (COMPANY_NAME, 'Company'),
        (ADDRESS, 'Address'),
        (JOB, 'Job'),
        (EMAIL, 'Email'),
        (PHONE_NUMBER, 'Phone number'),
        (DOMAIN, 'Domain name'),
        (DATE, 'Date'),
    )
    fixture = models.ForeignKey('factories.DataFixture', on_delete=models.CASCADE, related_name='columns')
    name = models.CharField(max_length=120)
    sample = models.PositiveSmallIntegerField(choices=SAMPLES, blank=False)
    order = models.PositiveSmallIntegerField(default=0)
    extra = IntegerRangeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.name}'

    class Meta:
        ordering = ['order']

    def generate_fake_data(self):
        column_types = {
            self.FULL_NAME: Faker().name(),
            self.INTEGER: randrange(self.extra.lower, self.extra.upper) if self.extra else 0,
            self.COMPANY_NAME: Faker().company(),
            self.ADDRESS: Faker().address(),
            self.JOB: Faker().job(),
            self.EMAIL: Faker().email(),
            self.PHONE_NUMBER: Faker().phone_number(),
            self.DOMAIN: Faker().domain_name(),
        }
        return column_types.get(self.sample)


class DataSet(models.Model):
    fixture = models.ForeignKey('factories.DataFixture', on_delete=models.CASCADE, related_name='datasets')
    task_id = models.UUIDField()
    filename = models.CharField(max_length=125)
    status = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.task_id} - {self.status}'

    class Meta:
        ordering = ['-created']
