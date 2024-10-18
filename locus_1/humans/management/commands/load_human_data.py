import openpyxl
from django.core.management import BaseCommand

from core.constants import LOCUSES
from humans.models import Human


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Human.objects.exists():
            self.stdout.write('Human table is not empty')

        self.stdout.write('Loading Human data...')

        book = openpyxl.open('../excel_data/real_data.xlsx')
        sheet = book.active

        human_counter = 0

        for column_index in range(1, sheet.max_column, 2):
            human = Human()

            row_index = 3
            for locus in LOCUSES:
                locus_1 = locus + '_1'
                locus_2 = locus + '_2'

                locus_1_value = sheet[row_index][column_index].value
                locus_2_value = sheet[row_index][column_index + 1].value

                row_index += 1

                setattr(human, locus_1, locus_1_value)
                setattr(human, locus_2, locus_2_value)

            human.save()
            human_counter += 1
            if human_counter % 40 == 0:
                self.stdout.write(f'Loaded {human_counter} humans...')

        book.close()

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded'
                                             f' {human_counter} humans!'))
