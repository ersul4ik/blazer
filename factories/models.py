from django.db import models


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


class DataFixtureColumn(models.Model):
    FULL_NAME = 1
    INTEGER = 2
    COMPANY = 3
    ADDRESS = 4
    SAMPLES = (
        (FULL_NAME, 'Full name'),
        (INTEGER, 'Integer'),
        (COMPANY, 'Company'),
        (ADDRESS, 'Address'),
    )
    fixture = models.ForeignKey('factories.DataFixture', on_delete=models.CASCADE, verbose_name='columns')
    name = models.CharField(max_length=120)
    sample = models.PositiveSmallIntegerField(choices=SAMPLES, blank=False)
    extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.name}'
