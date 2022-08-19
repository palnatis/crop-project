from application import app


def test_get_weather():
    test_client = app.test_client(False)
    result = test_client.get('/api/weather')
    assert result.status_code == 200


def test_get_yield():
    test_client = app.test_client(False)
    result = test_client.get('/api/yield')
    assert result.status_code == 200


def test_get_weather_stats():
    test_client = app.test_client(False)
    result = test_client.get('/api/weather/stats')
    assert result.status_code == 200


def test_get_weather_with_typo():
    test_client = app.test_client(False)
    result = test_client.get('/api/wheather')
    assert result.status_code == 404
