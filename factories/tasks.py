from io import BytesIO

import xlsxwriter
from celery import shared_task

from config.storages import PublicMediaStorage
from factories.models import DataFixture


@shared_task
def generate_data_set(fixture_id, row_count, filename):
    try:
        output = BytesIO()
        fixture = DataFixture.objects.get(id=fixture_id)
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        column_number = 0
        for text in fixture.columns.values_list('name', flat=True):
            worksheet.write(0, column_number, text)
            column_number += 1

        for i in range(1, row_count + 1):
            worksheet.write_row(i, 0, fixture.prepare_fake_data())

        workbook.close()
        storage = PublicMediaStorage()
        storage.save(filename, output)
        return filename
    except DataFixture.DoesNotExist:
        return
