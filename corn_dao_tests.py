from unittest.mock import MagicMock

import mock
from project.models.corn_dao import CornYieldDao


@mock.patch('project.models.corn_dao.db.cursor')
def test_insert_record(m_db):
    m_obj = MagicMock()
    m_db.side_effect = [m_obj]
    m_obj.execute.side_effect = ["None"]
    s = CornYieldDao('1', '100')
    s.insert_record()
    assert "insert into" in m_obj.execute.call_args[0][0].lower()
    assert m_db.called


@mock.patch('project.models.corn_dao.db.cursor')
def test_get_corn_yield_data(m_db):
    m_obj = MagicMock()
    m_db.side_effect = [m_obj]
    m_obj.execute.side_effect = ["None"]
    CornYieldDao.get_corn_yield_data(1, 19)
    sql = "select * from `corn_yield` limit 0, 19"
    assert m_db.called
    assert m_obj.execute.call_args[0][0] == sql
