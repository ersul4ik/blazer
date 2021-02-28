import xlsxwriter
from celery import shared_task
from django.utils import timezone

from factories.models import DataFixture


@shared_task
def generate_data_set(fixture_id, row_count):
    try:
        fixture = DataFixture.objects.get(id=fixture_id)
        filename = f'media/{fixture}-{timezone.now().strftime("%Y-%m-%d %H:%M:%S")}.xlsx'
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()

        column_number = 0
        for text in fixture.columns.values_list('name', flat=True):
            worksheet.write(0, column_number, text)
            column_number += 1

        for i in range(1, row_count + 1):
            worksheet.write_row(i, 0, fixture.prepare_fake_data())

        workbook.close()
        return filename
    except DataFixture.DoesNotExist:
        return
