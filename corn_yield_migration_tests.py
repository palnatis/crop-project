import mock
from corn_yield_migration import insert_data


@mock.patch('corn_yield_migration.CornYieldDao')
def test_insert_records(m_insert):
    count = insert_data("text_data/yld_data/US_corn_grain_yield.txt")
    assert m_insert.called
    assert count == 30
