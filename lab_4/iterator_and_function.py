import csv
import os
import re
from os.path import relpath
from typing import Optional


def iterator(name: str) -> Optional[str]:
    """create a csv"""
    names = os.listdir(os.path.join("Dataset", name))
    for i in range(len(names)):
        yield os.path.join("Dataset", name, names[i])  # делаем итератор
    return None


class Iterator:
    def __init__(self, way_to_csv_file: str, name_class: str):
        self.name_class = str(name_class)
        self.list = []
        self.way_to_file = way_to_csv_file
        self.counter = 0
        file = open(self.way_to_file, "r")
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            if str(row)[-3] == self.name_class:
                self.list.append(row)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.list):
            self.counter += 1
            return self.list[self.counter - 1]
        else:
            return ""

for i in iterator("5"):
    print(i)
