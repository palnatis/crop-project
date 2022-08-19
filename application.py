from flask import Flask, request, jsonify

from project.models.corn_dao import CornYieldDao
from project.models.data_analysis_dao import StatisticsDao
from project.models.weather_dao import WeatherDao

app = Flask(__name__)


@app.route('/api/weather', methods=['GET'])
def get_weather():
    """
    Gets Weather data from weather table
    :args:
        station_id(str): determines which station to look for
        date(str): filter criteria for weather data
        page(int): Page number to fetch
        limit(int): Number of records to fetch
    :return:
        json: corn yield details
    """
    station_id = request.args.get('station_id')
    date = request.args.get('date')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    if page <= 0 or limit <= 0:
        raise Exception("Page/limit can't be negative number")

    data = WeatherDao.get_weather_records(station_id, date, page, limit)
    result = {}
    counter = 1
    for record in data:
        result[counter] = {}
        result[counter]['State ID'] = record[0]
        result[counter]['Date'] = record[1].strftime("%Y-%b-%d")
        result[counter]['Max Temperature'] = record[2]
        result[counter]['Min Temperature'] = record[3]
        result[counter]['precipitation'] = record[4]
        counter += 1
    return jsonify(result)


@app.route('/api/yield', methods=['GET'])
def get_yield():
    """
    Gets Corn Yield data from corn_yield table
    :args:
        page(int): Page number to fetch
        limit(int): Number of records to fetch
    :return:
        json: corn yield details
    """
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    if page <= 0 or limit <= 0:
        raise Exception("Page/limit can't be negative number")

    data = CornYieldDao.get_corn_yield_data(page, limit)
    result = {}
    counter = 1
    for record in data:
        result[counter] = {}
        result[counter]['Year'] = record[0]
        result[counter]['Yield'] = record[1]
        counter += 1
    return jsonify(result)


@app.route('/api/weather/stats', methods=['GET'])
def get_weather_stats():
    """
    Get Weather statistics from data_statistics table
    :args:
        page(int): Page number to fetch
        limit(int): Number of records to fetch
    :return:
        json: statistics
    """
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    # validation to check page number and limit or not negative numbers
    if page <= 0 or limit <= 0:
        raise Exception("Page/limit can't be negative number")

    data = StatisticsDao.get_stats_data(page, limit)
    result = {}
    counter = 1
    # parsing query output to dict
    for record in data:
        result[counter] = {}
        result[counter]['State ID'] = record[0]
        result[counter]['Year'] = record[1]
        result[counter]['Avg max temp'] = str(record[2])
        result[counter]['Avg min temp'] = str(record[3])
        result[counter]['Total precipitation'] = record[4]
        counter += 1

    return jsonify(result)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
