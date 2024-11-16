import csv
import os
import sys

from loguru import logger
from os.path import relpath
from tqdm import trange

logger.add(sys.stderr, level="INFO", format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")


def first_script(path_dir: str)->str:
    file_name = "test_csv.csv"
    try:
        os.chdir(path_dir)
        logger.info(
            f"The current working directory has been changed to {path_dir}")
        out_directory = os.path.dirname(__file__)
        with open(file_name, mode="w") as w_file:
            writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
            writer.writerow(("absolut path", "relativ path", "quote"))  # Заголовки столбца
            for star in trange(1, 6):
                directory = os.path.join(out_directory, "Dataset", str(star))
                for dirs, folder, files in os.walk(directory):
                    for element in files:
                        writer.writerow([path_dir + "/" + element, "Dataset" + '/' + str(star) + "/" + element, star])
        print("adf")
        logger.info(f"The file {file_name} has been processed successfully")
    except Exception as ex:
        logger.error(
            f"The file {file_name} was not found: {ex.message}\n{ex.args}\n"
        )
