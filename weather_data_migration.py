import os
from argparse import ArgumentParser
from datetime import datetime

from project.logger import get_logger
from project.models.weather_dao import WeatherDao

log = get_logger('weather_ingestion.log')


def insert_data(file_name):
    """
    Inserts Weather data from given file to the Database
    :param
        file_name: File containing raw data
    :return:
        count(int): Number of records inserted
    """
    file = open(file_name, 'r')
    station_id = os.path.basename(file_name).split(".")[0]
    count = 0
    for f in file.readlines():
        try:
            data = f.split("\t")
            data = [i.strip() for i in data]
            w = WeatherDao(station_id, data[0], data[1], data[2], data[3])
            w.insert_record()
            count += 1
        except Exception as e:
            pass

    return count


if __name__ == "__main__":
    """
    Use -h or --help to understand runtime parameters
    """
    parser = ArgumentParser()
    parser.add_argument("-f",  help="File to read data")
    parser.add_argument("-d", help="Directory to read data")

    args = parser.parse_args()
    if args.f and args.d:
        print("Pass either File or Directory")
        exit(0)
    if not args.f and not args.d:
        print("Pass either File or Directory")
        exit(0)
    if args.f:
        started = datetime.now()
        log.info("Started Data Ingestion")
        count = insert_data(args.f)
        end = datetime.now() - started
        log.info(f"Completed ingestion in {end}, inserted {count} records")
    if args.d:
        started = datetime.now()
        log.info("Started Weather Data Ingestion")
        list_dir = os.listdir(args.d)
        count = 0
        for f in list_dir:
            file_name = os.path.join(args.d, f)
            count += insert_data(file_name)
            log.info(f"Done with {f}")
        end = datetime.now() - started
        log.info(f"Completed Weather data ingestion in {end}, "
                 f"inserted {count} records")
