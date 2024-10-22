import csv
import json
import logging
import os
import pandas as pd
import re

logging.basicConfig(level=logging.INFO)


def is_valid(name_csv: str) -> None:
    try:
        s = 0
        rows = []
        with open(f'{name_csv}.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            header = next(csv_reader)
            for row in csv_reader:
                rows.append(row)
        print(header)
        for i in range(len(rows)):
            match header[9]:
                case 'email':
                    if not re.fullmatch(re_email, rows[i][0]):
                        s += 1
                        print(i, ' = ', rows[i][0])
                case 'http_status_message':
                    if not re.fullmatch(re_http_status_message, rows[i][1]):
                        s += 1
                        print(i, ' = ', rows[i][1])
                case 'inn':
                    if not re.fullmatch(re_inn, rows[i][2]):
                        s += 1
                        print(i, ' = ', rows[i][2])
                case 'passport':
                    if not re.fullmatch(re_passport, rows[i][3]):
                        s += 1
                        print(i, ' = ', rows[i][3])
                case 'ip_v4':
                    if not re.fullmatch(re_ip_v4, rows[i][4]):
                        s += 1
                        print(i, ' = ', rows[i][4])
                case 'latitude':
                    if not re.fullmatch(re_latitude, rows[i][5]):
                        s += 1
                        print(i, ' = ', rows[i][5])
                case 'hex_color':
                    if not re.fullmatch(re_hex_color, rows[i][6]):
                        s += 1
                        print(i, ' = ', rows[i][6])
                case 'isbn':
                    if not re.fullmatch(re_isbn, rows[i][7]):
                        s += 1
                        print(i, ' = ', rows[i][7])
                case 'uuid':
                    if not re.fullmatch(re_uuid, rows[i][8]):
                        s += 1
                        print(i, ' = ', rows[i][8])
                case 'time':
                    if not re.fullmatch(re_time, rows[i][9]):
                        s += 1
                        print(i, ' = ', rows[i][9])
        print(s)
    except:
        logging.error(f'Error in is_valid')


if __name__ == "__main__":
    re_email = re.compile(
        r'([\dA-Za-z]+[\.-_])*[\dA-Za-z]+@[-\dA-Za-z]+(\.[A-Z|a-z]{2,})+')
    re_http_status_message = re.compile(r'(\d{3})( [a-zA-Z]{2,})+')
    re_inn = re.compile(r'(\d{12})')
    re_passport = re.compile(r'(\d{2} ){2}(\d{6})')
    re_ip_v4 = re.compile(r'(\d{1,3}[\.]){3}\d{1,3}')
    re_latitude = re.compile(r'[+-]?\d{1,}\.\d{1,}')
    re_hex_color = re.compile(r'#([\da-fA-F]{6})')
    re_isbn = re.compile(r'(\d{3}-)?\d-(\d{5})-(\d{3})-\d')
    re_uuid = re.compile(r'([\da-f]{8})-([\da-f]{4}-){3}([\da-f]{12})')
    re_time = re.compile(r'([0-1]\d|2[0-3])(:[0-5]\d){2}\.(\d{6})')
    is_valid('lab_3\85')
