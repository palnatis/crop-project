from datetime import datetime

from project.database import db
from project.logger import get_logger
from project.models.data_analysis_dao import StatisticsDao

log = get_logger('stats.log')

# Query to find
# Average maximum temperature (in degrees Celsius)
# Average minimum temperature (in degrees Celsius)
# Total accumulated precipitation (in centimeters)
# for every year, for every weather station
sql = """
select station_id, year(`date`) as `year`,
avg(case when max_temperature!=-9999 then max_temperature end) as avg_max,
avg(case when min_temperature!=-9999 then min_temperature end) as avg_min,
sum(case when precipitation!=-9999 then precipitation end) as
total_precipitation
from weather
group by station_id, `year`;
"""
started = datetime.now()
log.info("Started analysing data")
cursor = db.cursor()
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    s_dao = StatisticsDao(result[0], result[1],
                          result[2], result[3],
                          result[4])
    try:
        s_dao.insert_record()
    except Exception as e:
        pass
end = datetime.now() - started
log.info(f"Completed analysing in {end}")
