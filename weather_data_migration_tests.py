from unittest import mock

from weather_data_migration import insert_data


@mock.patch('weather_data_migration.WeatherDao')
def test_insert_records(m_insert):
    count = insert_data("text_data/wx_data/USC00110072.txt")
    assert m_insert.called
    assert count == 10865
