import random
import csv
from os import getcwd
from loguru import logger
holding_value = []
coil_value = []
input_value = []
temp_header = ["temp_key", "temp_value"]


def creating_csv_file(file):
    try:
        write_csv_file = open(f'{getcwd()}/modbus/{file}', "w+")
        writer = csv.writer(write_csv_file)
        count = 0
        logger.debug(f"file {file} is writing started please wait....")
        if file == "holding.csv":
            for data in holding_value:
                if count == 0:
                    header = data.keys()
                    writer.writerow(header)
                    count += 1
                writer.writerow(data.values())
        elif file == "input.csv":
            for data in input_value:
                if count == 0:
                    header = data.keys()
                    writer.writerow(header)
                    count += 1
                writer.writerow(data.values())
        elif file == "coil.csv":
            for data in coil_value:
                if count == 0:
                    header = data.keys()
                    writer.writerow(header)
                    count += 1
                writer.writerow(data.values())
    except Exception as e:
        logger.error(str(e))


def creating_json_for_hold_input(i, j, k, file):
    try:
        for key_ in range(j, (k+1)):
            data = {}
            value_ = random.randint(i, (k-1))
            data.update({temp_header[0]: key_})
            data.update({temp_header[1]: value_})
            if file == "holding.csv":
                holding_value.append(data)
            elif file == "input.csv":
                input_value.append(data)
    except Exception as e:
        logger.error(str(e))


def creating_json_for_coil(i, j, k, file):
    try:
        for key_ in range(j, (k+1)):
            data = {}
            value_ = random.randint(i, j)
            data.update({temp_header[0]: key_})
            data.update({temp_header[1]: value_})
            coil_value.append(data)
    except Exception as e:
        logger.error(str(e))


if __name__ == "__main__":
    i = 0
    j = 1
    k = 65536
    temp_filename = ["input.csv", "holding.csv", "coil.csv"]
    try:
        for file in temp_filename:
            if file == "holding.csv":
                creating_json_for_hold_input(i, j, k, file)
                creating_csv_file(file)
                logger.info(f"file is successfully created in {getcwd()}/modbus/{file}")
            elif file == "coil.csv":
                creating_json_for_coil(i, j, k, file)
                creating_csv_file(file)
                logger.info(f"file is successfully created in {getcwd()}/modbus/{file}")
            elif file == "input.csv":
                creating_json_for_hold_input(i, j, k, file)
                creating_csv_file(file)
                logger.info(f"file is successfully created in {getcwd()}/modbus/{file}")
    except Exception as e:
        logger.error(str(e))
