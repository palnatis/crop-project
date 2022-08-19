from argparse import ArgumentParser
from datetime import datetime

from project.logger import get_logger
from project.models.corn_dao import CornYieldDao

log = get_logger('corn_yield_ingestion.log')


def insert_data(file_name):
    """
    Inserts Corn Yield data from given file to the Database
    :param
        file_name: File containing raw data
    :return:
        count(int): Number of records inserted
    """
    file = open(file_name, 'r')
    count = 0
    for f in file.readlines():
        try:
            data = f.split("\t")
            data = [i.strip() for i in data]
            c = CornYieldDao(data[0], data[1])
            c.insert_record()
            count += 1
        except Exception as e:
            print(e)

    return count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f",  help="File to read data")
    args = parser.parse_args()

    if not args.f:
        print("Pass File")
        exit(0)
    if args.f:
        started = datetime.now()
        log.info("Started Corn Yield Data ingestion")
        count = insert_data(args.f)
        end = datetime.now() - started
        log.info(f"Completed Corn Yield Data ingestion in {end}, "
                 f"inserted {count} records")
