import mock
from unittest.mock import MagicMock

from project.models.weather_dao import WeatherDao


@mock.patch('project.models.weather_dao.db.cursor')
def test_insert_record(m_db):
    m_obj = MagicMock()
    m_db.side_effect = [m_obj]
    m_obj.execute.side_effect = ["None"]
    s = WeatherDao('1', '100', 1, 2, 3)
    s.insert_record()
    assert "insert into" in m_obj.execute.call_args[0][0].lower()
    assert m_db.called


@mock.patch('project.models.weather_dao.db.cursor')
def test_get_corn_yield_data(m_db):
    m_obj = MagicMock()
    m_db.side_effect = [m_obj]
    m_obj.execute.side_effect = ["None"]
    WeatherDao.get_weather_records(1, 19, 1, 1)
    sql = "select * from `weather` where station_id='1' " \
          "and date='19' limit 0, 1"
    assert m_db.called
    assert m_obj.execute.call_args[0][0] == sql
