import csv
import os
import random
import sys

from loguru import logger
from tqdm import tqdm

logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")


def script_three(path_dir: str) -> str:
    os.chdir(path_dir)
    logger.info(
        f"The current working directory has been changed to {path_dir}")
    file_name = "test_csv_three.csv"
    names = [i for i in range(10000)]
    try:
        with open(file_name, mode="w") as w_file:
            writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
            writer.writerow(("absolut path", "relativ path", "quote"))
            pbar = tqdm(os.listdir("dataset_two"), ncols=100, colour='green')
            for element in pbar:
                name = random.choice(names)
                names.remove(name) 
                try:
                    with open(os.path.join("dataset_two", element), "rb") as f:
                        text = f.read()
                    logger.info(
                        f"The file dataset_two has been processed successfully"
                    )
                except Exception as ex:
                    logger.error(
                        f"The file dataset_two cannot be read: {ex.message}\n{ex.args}\n"
                    ) 
                try:
                    with open(os.path.join("dataset_three", str(name) + ".txt"), "wb") as f:
                        f.write(text)
                    logger.info(
                        f"The file dataset_three has been processed successfully"
                    )
                except Exception as ex:
                    logger.error(
                        f"The file dataset_three cannot be processed: {ex.message}\n{ex.args}\n"
                    ) 
                directory = os.path.join(path_dir, "dataset_three", str(name) + ".txt")
                writer.writerow([directory, os.path.join("dataset_two", element), element[0]])
        logger.info(f"The file {file_name} has been processed successfully")
    except Exception as ex:
        logger.error(f"The file {file_name} was not found: {ex.message}\n{ex.args}\n")
