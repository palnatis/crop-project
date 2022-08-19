import mock
from unittest.mock import MagicMock

from project.models.data_analysis_dao import StatisticsDao


@mock.patch('project.models.data_analysis_dao.db.cursor')
def test_insert_record(m_db):
    m_obj = MagicMock()
    m_db.side_effect = [m_obj]
    m_obj.execute.side_effect = ["None"]
    s = StatisticsDao('1', '100', 1, 2, 3)
    s.insert_record()
    assert "insert into" in m_obj.execute.call_args[0][0].lower()
    assert m_db.called


@mock.patch('project.models.data_analysis_dao.db.cursor')
def test_get_corn_yield_data(m_db):
    m_obj = MagicMock()
    m_db.side_effect = [m_obj]
    m_obj.execute.side_effect = ["None"]
    StatisticsDao.get_stats_data(1, 19)
    sql = "select * from `data_statistics` limit 0, 19"
    assert m_db.called
    assert m_obj.execute.call_args[0][0] == sql
