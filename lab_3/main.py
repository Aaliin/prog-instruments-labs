import csv
import logging
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 85
PARH_VARIANT = f'lab_3\{VARIANT}'
PATTERNS = {
    're_email': r'([\dA-Za-z]+[\.-_])*[\dA-Za-z]+@[-\dA-Za-z]+(\.[A-Z|a-z]{2,})+',
    're_http_status_message': r'(\d{3})( [a-zA-Z]{2,})+',
    're_inn': r'(\d{12})',
    're_passport': r'(\d{2} ){2}(\d{6})',
    're_ip_v4': r'((25[0-5]|2[0-4]\d|1\d\d|\d{,2})\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d{,2})',
    're_latitude': r'[+-]?\d{1,}\.\d{1,}',
    're_hex_color': r'#([\da-fA-F]{6})',
    're_isbn': r'(\d{3}-)?\d-(\d{5})-(\d{3})-\d',
    're_uuid': r'([\da-f]{8})-([\da-f]{4}-){3}([\da-f]{12})',
    're_time': r'([0-1]\d|2[0-3])(:[0-5]\d){2}\.(\d{6})',
}

logging.basicConfig(level=logging.INFO)


def invalid(name_csv: str) -> list:
    '''Осуществляет проверку столбцов csv-файла на валидность

    Args:
        name_csv(str) - путь к файлу, необходимый для открытия

    Returns:
        list - список номеров строк с невалиднами данными
    '''
    try:
        all_invalid = 0
        number_rows = set()
        with open(f'{name_csv}.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            header = next(csv_reader)
            for index, row in enumerate(csv_reader):
                for regular, value in zip(PATTERNS.keys(), row):
                    pattern = PATTERNS[regular]
                    if not re.fullmatch(pattern, str(value)):
                        number_rows.add(index)
                        all_invalid += 1
        list_for_sum = list(number_rows)
        print(f'Types of data used:', ', '.join(header))
        print(f'Checksum of invalid elements:', sum(list_for_sum))
        print(f'The total number of invalid values: {all_invalid}')
        return list_for_sum
    except Exception as ex:
        logging.error(
            f'Incorrect data has been entered: {ex.message}\n{ex.args}\n')


if __name__ == "__main__":
    list_invalid = invalid(PARH_VARIANT)
    print(f'Hash of the checksum:', calculate_checksum(list_invalid))
    serialize_result(VARIANT, calculate_checksum(list_invalid))
