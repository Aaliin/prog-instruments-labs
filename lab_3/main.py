import csv
import logging
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 85
PARH_VARIANT = f'lab_3\{VARIANT}'

logging.basicConfig(level=logging.INFO)


def invalid(name_csv: str) -> list:
    '''Осуществляет проверку столбцов csv-файла на валидность

    Args:
        name_csv(str) - путь к файлу, необходимый для открытия

    Returns:
        list - список номеров строк с невалиднами данными
    '''
    try:
        rows = []
        all_invalid = 0
        number_rows = set()
        with open(f'{name_csv}.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            header = next(csv_reader)
            for row in csv_reader:
                rows.append(row)
        print(f'Types of data used:', ', '.join(header))
        for i in range(len(rows)):
            if (not re.fullmatch(re_email, rows[i][0])
                    or not re.fullmatch(re_http_status_message, rows[i][1])
                    or not re.fullmatch(re_inn, rows[i][2])
                    or not re.fullmatch(re_passport, rows[i][3])
                    or not re.fullmatch(re_ip_v4, rows[i][4])
                    or not re.fullmatch(re_latitude, rows[i][5])
                    or not re.fullmatch(re_hex_color, rows[i][6])
                    or not re.fullmatch(re_isbn, rows[i][7])
                    or not re.fullmatch(re_uuid, rows[i][8])
                    or not re.fullmatch(re_time, rows[i][9])):
                number_rows.add(i)
                all_invalid += 1
        list_for_sum = list(number_rows)
        print(f'Checksum of invalid elements:', sum(list_for_sum))
        print(f'The total number of invalid values: {all_invalid}')
        return list_for_sum
    except Exception as ex:
        logging.error(
            f'Incorrect data has been entered: {ex.message}\n{ex.args}\n')


if __name__ == "__main__":
    re_email = re.compile(
        r'([\dA-Za-z]+[\.-_])*[\dA-Za-z]+@[-\dA-Za-z]+(\.[A-Z|a-z]{2,})+')
    re_http_status_message = re.compile(r'(\d{3})( [a-zA-Z]{2,})+')
    re_inn = re.compile(r'(\d{12})')
    re_passport = re.compile(r'(\d{2} ){2}(\d{6})')
    re_ip_v4 = re.compile(
        r'((25[0-5]|2[0-4]\d|1\d\d|\d{,2})\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d{,2})')
    re_latitude = re.compile(r'[+-]?\d{1,}\.\d{1,}')
    re_hex_color = re.compile(r'#([\da-fA-F]{6})')
    re_isbn = re.compile(r'(\d{3}-)?\d-(\d{5})-(\d{3})-\d')
    re_uuid = re.compile(r'([\da-f]{8})-([\da-f]{4}-){3}([\da-f]{12})')
    re_time = re.compile(r'([0-1]\d|2[0-3])(:[0-5]\d){2}\.(\d{6})')

    list_invalid = invalid(PARH_VARIANT)
    print(f'Hash of the checksum:', calculate_checksum(list_invalid))
    serialize_result(VARIANT, calculate_checksum(list_invalid))
