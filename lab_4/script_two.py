import csv
import os
import sys

from loguru import logger
from tqdm import tqdm
from os.path import relpath
import first_script

file_name = "test_csv.csv"
file_name_two = "test_csv_two.csv"

logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")


def script_two(path_dir: str) -> str:
    out_directory = os.path.dirname(__file__)
    os.chdir(path_dir)
    logger.info(f"The current working directory has been changed to {path_dir}")
    try:
        with open(file_name_two, mode="w") as w_file:
            writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
            writer.writerow(("absolut path", "relativ path", "quote"))  # Заголовки столбца
        logger.info(f"The file {file_name_two} has been processed successfully")
    except Exception as ex:
        logger.error(
            f"The file {file_name_two} was not found: {ex.message}\n{ex.args}\n"
        )
    if not os.path.isfile(file_name):   first_script.first_script(path_dir)
    try:
        with open("test_csv.csv", "r") as fh:
            reader = csv.reader(fh)
            spisok = list(reader)
            if not os.path.isdir("dataset_two"):
                os.makedirs("dataset_two")
            pbar = tqdm(spisok, ncols=100, colour='green')
            content = False
            for element in pbar:
                if content:
                    print(element[0])
                    os.chdir(out_directory)
                    logger.info(
                        f"The current working directory has been changed to {out_directory}"
                    )
                    try:
                        with open(element[1], "rb") as f:
                            text = f.read()
                            namefile = element[1].split("/")
                    except Exception as ex:
                        logger.error(
                            f"No file with that name was found: {ex.message}\n{ex.args}\n"
                        )
                    os.chdir(path_dir)
                    with open(os.path.join("dataset_two", element[2] + "_" + namefile[2]), "wb") as f:
                        f.write(text)
                    with open(file_name_two, mode="a") as w_file:
                        writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
                        writer.writerow([path_dir + "/dataset_two/" + element[2] + "_" + namefile[2],
                                        path_dir + "dataset_two/" + element[2] + "_" + namefile[2], element[2]])
                content = True
    except Exception as ex:
        logger.error(
            f"The file test_csv.csv was not found: {ex.message}\n{ex.args}\n"
        )
